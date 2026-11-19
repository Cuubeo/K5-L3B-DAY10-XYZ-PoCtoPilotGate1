"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from datetime import date

from . import helpers as H  # noqa: F401
from .tools import Verdict


def _approval_problem(ctx, action, order, policy):
    amount = action.get("amount_vnd")
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        return "số tiền hoàn không hợp lệ"

    approval_id = action.get("approval_id")
    required = amount > policy["auto_limit_vnd"] and action.get("payer") != "MERCHANT"
    if not approval_id:
        return "thiếu phê duyệt cho khoản vượt hạn mức tự động" if required else None

    approvals = ctx.tools.lookup_approvals(approval_id=approval_id)
    if len(approvals) != 1:
        return "không tìm thấy duy nhất một bản ghi phê duyệt"
    approval = approvals[0]
    approver_id = ctx.gates.get("operations", {}).get("approver_id")

    expires_at = approval.get("expires_at")
    if not isinstance(expires_at, str) or not isinstance(ctx.as_of, str):
        return "thiếu ngày hết hạn hoặc ngày đối chiếu"
    try:
        expiry = date.fromisoformat(expires_at)
        as_of = date.fromisoformat(ctx.as_of)
    except ValueError:
        return "ngày phê duyệt không hợp lệ"

    max_vnd = approval.get("max_vnd")
    if (approval.get("ticket_id") != action.get("ticket_id")
            or approval.get("ticket_id") != ctx.ticket.get("ticket_id")
            or approval.get("order_id") != action.get("order_id")
            or approval.get("customer_id") != ctx.ticket.get("customer_id")
            or approval.get("customer_id") != order.get("customer_id")
            or (approver_id and approval.get("approver_id") != approver_id)
            or approval.get("status") != "valid"
            or expiry < as_of
            or not isinstance(max_vnd, (int, float))
            or isinstance(max_vnd, bool)
            or max_vnd < amount):
        return "phê duyệt sai ticket/đơn/khách/duyệt viên, hết hạn, bị thu hồi hoặc không đủ hạn mức"
    return None


def _auto_rows_today(ctx):
    """Các dòng hoàn TỰ ĐỘNG (không có approval_id) được ghi trong ngày hôm nay.

    ledger_rows() trả cả sổ cái cũ (ledger_seed, các ngày trước). Sổ cái chỉ ghi nối vào cuối, nên các dòng của hôm
    nay nằm ở cuối danh sách. Đi ngược từ cuối, cộng dồn dòng tự động cho tới khi bằng auto_refund_today_vnd()
    (tổng hoàn tự động hôm nay do host tính); mọi khoản hoàn đều > 0 nên điểm cắt là duy nhất.
    """
    target = ctx.tools.auto_refund_today_vnd()
    today, acc = [], 0
    for row in reversed(ctx.tools.ledger_rows()):
        if acc >= target:
            break
        if row.get("approval_id"):
            continue
        today.append(row)
        acc += row.get("amount_vnd") or 0
    return today if acc == target else [r for r in ctx.tools.ledger_rows() if not r.get("approval_id")]


def _customer_refund_cap_problem(ctx, action, order):
    cap = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
    if cap is None or action.get("approval_id"):
        return None

    customer_id = order.get("customer_id")
    spent = sum(row["amount_vnd"] for row in _auto_rows_today(ctx) if row.get("customer_id") == customer_id)
    amount = action["amount_vnd"]
    if spent + amount > cap:
        ctx.log("customer_refund_cap", customer_id=customer_id, spent_vnd=spent,
                proposed_vnd=amount, cap_vnd=cap)
        return "vượt trần hoàn tự động mỗi khách trong ngày"
    return None


def pre_guard(ctx):
    # Cổng vòng 1 (HAZOP B4 dòng INVALID, drift B3): agent tự chọn chính sách theo cờ index_active, có thể lệch
    # ngày hiệu lực (v3 hết 2026-11-30, v4 từ 2026-12-01). Ghim phiên bản theo ngày hôm nay từ nguồn sự thật.
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        ctx.log("no_effective_policy", as_of=ctx.as_of)
        return Verdict.escalate("không có chính sách hoàn tiền nào hiệu lực vào ngày này; chuyển người duyệt")
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault"):
        return Verdict.allow()

    order_id = action.get("order_id")
    if order_id != ctx.ticket.get("order_id"):
        ctx.log("source_fact_mismatch", tool=tool, order_id=order_id)
        return Verdict.escalate("đơn trong lệnh ghi không khớp ticket")

    order = ctx.tools.lookup_order(order_id)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if order is None or policy is None:
        ctx.log("source_fact_unavailable", tool=tool, order_id=order_id)
        return Verdict.escalate("không tra được đơn hoặc chính sách đang hiệu lực")

    if tool == "issue_refund":
        approval_problem = _approval_problem(ctx, action, order, policy)
        if approval_problem:
            ctx.log("invalid_approval", approval_id=action.get("approval_id"), reason=approval_problem)
            return Verdict.escalate(f"{approval_problem}; chuyển người duyệt")

        customer_cap_problem = _customer_refund_cap_problem(ctx, action, order)
        if customer_cap_problem:
            return Verdict.escalate(f"{customer_cap_problem}; chuyển người duyệt")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)
        proposal = next((e for e in reversed(ctx.events) if e.get("type") == "proposal"), None)
        if proposal is None or proposal.get("delay_days_used") != delay:
            ctx.log("refund_delay_mismatch", order_id=order_id, db_delay_days=delay,
                    proposed_delay_days=(proposal or {}).get("delay_days_used"))
            return Verdict.escalate("độ trễ đề xuất không khớp tracking; cần người duyệt")

        entitlement = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        if action.get("amount_vnd", 0) > entitlement:
            ctx.log("refund_over_entitlement", order_id=order_id, amount_vnd=action.get("amount_vnd"),
                    entitlement_vnd=entitlement)
            return Verdict.escalate("số tiền hoàn vượt quyền lợi theo tracking và chính sách")
        if proposal.get("do_fault") and not H.carrier_at_fault(policy, parcel, delay):
            ctx.log("carrier_fault_without_evidence", order_id=order_id, parcel_id=parcel["parcel_id"])
            return Verdict.escalate("chưa đủ dữ liệu tracking để quy lỗi cho hãng")
        return Verdict.allow()

    parcel = next((p for p in order.get("parcels", []) if p.get("parcel_id") == action.get("parcel_id")), None)
    if parcel is None:
        ctx.log("carrier_fault_unknown_parcel", order_id=order_id, parcel_id=action.get("parcel_id"))
        return Verdict.escalate("không tìm thấy kiện hàng trong nguồn tracking")
    delay = H.db_delay_days(parcel, ctx.as_of)
    if (action.get("carrier_id") != parcel.get("carrier_id")
            or action.get("delay_days") != delay
            or not H.carrier_at_fault(policy, parcel, delay)):
        ctx.log("carrier_fault_without_evidence", order_id=order_id, parcel_id=parcel["parcel_id"],
                db_delay_days=delay, recorded_cause=parcel.get("delay_cause"))
        return Verdict.escalate("lệnh ghi lỗi hãng không khớp tracking và chính sách")
    return Verdict.allow()
