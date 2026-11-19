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
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    return Verdict.allow()


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
