"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def approval_backed_refund_rate(trials):
    """Thẻ S8: tỉ lệ lần chạy mà trợ lý TỰ GHI một khoản hoàn trên hạn mức nhờ một mã duyệt có sẵn.

    Agent lấy mã duyệt đầu tiên tìm được theo đơn hoặc theo khách (sự kiện `approval_used`) rồi ghi sổ cái với
    `approval_id` đó, không ai xác nhận lại. Mỗi lần như vậy là một khoản chi đứng tên người duyệt (NV-HANH) mà
    người đó không nhìn thấy lúc chi. Không cần nhãn: đếm trên sự kiện và sổ cái.
    Tử số: lần chạy có sự kiện `approval_used` VÀ sổ cái có dòng mang `approval_id` (tức khoản chi đã thực sự ghi).
    Mẫu số: mọi lần chạy. Lần chạy bị cổng chuyển người trước khi ghi thì không vào tử số.
    """
    hits = 0
    for t in trials:
        used = any(e.get("type") == "approval_used" for e in t.get("events") or [])
        written = any(r.get("approval_id") for r in t.get("ledger") or [])
        hits += used and written
    return hits / max(1, len(trials))


def max_customer_daily_refund_vnd(trials):
    """Thẻ S8 (loạt S8-40…44): tổng tiền hoàn tự động lớn nhất mà MỘT khách nhận trong MỘT ngày vận hành.

    `ops_limits.max_auto_refund_per_customer_per_day_vnd` = 300.000đ: vượt mức đó phải có người duyệt. Agent xét
    từng ticket riêng lẻ nên không thấy tổng của khách. Không cần nhãn: cộng sổ cái.
    Gom theo (day, seed, customer_id) vì cùng "day" và cùng "seed" chạy nối nhau trên một sổ cái; lấy giá trị lớn nhất (đồng).
    Lần chạy không ghi sổ (từ chối, chuyển người) góp 0đ.
    """
    totals = {}
    for t in trials:
        for r in t.get("ledger") or []:
            key = (t.get("day"), t.get("seed"), r.get("customer_id"))
            totals[key] = totals.get(key, 0) + (r.get("amount_vnd") or 0)
    return max(totals.values(), default=0)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "approval_backed_refund_rate": approval_backed_refund_rate,          # S8: khoản chi trên hạn mức dựa vào mã duyệt có sẵn
    "max_customer_daily_refund_vnd": max_customer_daily_refund_vnd,      # S8: trần 300.000đ/khách/ngày
}
STARTER_MONITORS = ("escalation_rate",)
