# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** K5-L3B-DAY10-XYZ-PoCtoPilotGate1 · **Thẻ đã bốc:** S8 *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S8-prepared-20261119-162602-aa8f8b` (grade `R-S8-grade-20261119-162600-aa8f8b`) | S8 · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | 0.8654 [0.7692; 0.9423] | 0.8654 | 6.845.000 · 35 · 0 | 0.0 (nhưng nhân viên kiểm lại 100% quyết định tự động) | Cổng vòng 1 không đỡ được gì: prepared trùng hệt base; hàng chờ 36 ca ùn, chờ lâu nhất 216 phút, chi phí 11.325đ/ticket > làm tay, ROI −2,44 |
| 2 | | Sx · after | | | | | | |
| 3 | | Sx · after | | | | | | |
| 4 | | base · after | (kiểm không regression) | | | | | |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S8-grade-20261119-162600-aa8f8b` · base: `R-S8-before-20261119-162602-aa8f8b` · prepared: `R-S8-prepared-20261119-162602-aa8f8b`
  *(Lần grade đầu `R-S8-grade-20261119-162243-3d00d7` báo `1 integrity ❌` do máy Windows đổi kiểu xuống dòng của file khoá; đã cố định bằng `.gitattributes`, nội dung file không đổi. Lần grade trên chạy lại khi chưa sửa gì: `1 integrity ✅`, `2 criteria ✅`.)*
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): **Không ô nào trên gói S8.** pass_rate 0,8654 → 0,8654, hoàn sai 6.845.000đ → 6.845.000đ, lỗi hãng oan 35 → 35, chờ lâu nhất 216 → 216 phút, ca ùn 36 → 36. Chỉ đổi phía chi phí: 11.225đ → 11.325đ/ticket, do `decision_note` thêm 100đ LLM. Trên bộ nền cổng vòng 1 vẫn giữ: hoàn sai 20.000đ → 0, lỗi hãng oan 1 → 0, `5 regression ✅`. Phần cấu hình vòng 1 đã đáp ứng 3/4 điều kiện để nhân viên thôi kiểm tay (`decision_note` = true, kiểm mẫu 10%, `approver_id` = NV-HANH), nhưng report vẫn ghi "Niềm tin của nhân viên duyệt: **chưa đạt** · còn thiếu: trong ngày vẫn có khoản hoàn dùng phê duyệt không hợp lệ", nên nhân viên vẫn kiểm lại 100%.
- Khối kinh doanh và vận hành còn dòng nào vượt trần: hàng chờ **36 ca bị ùn**; chờ lâu nhất **216 phút** > 60 phút; chi phí **11.325đ/ticket** > làm tay 10.000đ; **ROI −2,44** < 0,25; cả 4 kho CT, DN, HCM, HN đều đắt hơn làm tay (≈ 10.750đ/ticket); tiết kiệm ròng −1.437.921đ/ngày. Ngưỡng đã ký chưa đạt: pass_rate, wrongful_refund_vnd, wrongful_carrier_faults, cost_per_ticket_vnd, roi, queue_stuck. Report kết luận: **KHÔNG đủ căn cứ để chọn "Tiếp tục"**.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? Chính là **con người và vận hành** (trưởng ca không tin trợ lý, cả ca kiểm tay, hàng chờ ngập). Kéo theo **kinh doanh** (chi phí cao hơn làm tay, ROI âm) và **pháp lý** (NV-HANH bị ghi là người duyệt những khoản chị không duyệt). Gốc kỹ thuật cần dò: trợ lý dùng mã phê duyệt sai (sự kiện `approval_used`).
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? **Có một nửa.** B6 có dòng "Nhân viên CSKH không tin trợ lý, tự kiểm lại 100% quyết định bằng tay" và bàn đã đặt sẵn `decision_note`, kiểm mẫu 10%, `approver_id` = NV-HANH, nhưng xếp phần còn lại vào risk register. Cổng vòng 1 **không đỡ được con số nào** ở cột prepared. Bàn **không nghĩ tới** nguyên nhân khiến mất niềm tin: trợ lý tự dùng mã phê duyệt không hợp lệ (của ticket khác, hết hạn, đã thu hồi, vượt hạn mức). HAZOP B4 làm trên `file_carrier_fault`, không làm trên bước "tìm phê duyệt"; `write_gate` của bàn chỉ kiểm số tiền so với quyền lợi, không kiểm `approval_id`.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Trợ lý đã lấy đại một mã phê duyệt tìm được theo đơn hoặc theo khách (của ticket khác, hết hạn, đã thu hồi, hạn mức thấp hơn số tiền) để chi khoản trên 200.000đ; kiểm toán ghi NV-HANH là người duyệt | Kỹ thuật · Pháp lý | Trace sự kiện `approval_used` đối chiếu bảng `approvals` (`ticket_id`, `max_vnd`, `expires_at`, `status`) trong `incidents/S8/world_patch.json`; `lab10/agent.py` bước 5 lấy `cands[0]` |
| Nhân viên mất tin nên kiểm tay 100%: hàng chờ một người duyệt ngập (36 ca ùn, chờ 216 phút), chi phí cao hơn làm tay, pilot lỗ | Con người và vận hành · Kinh doanh | Report grade S8 khối kinh doanh và vận hành; `staff_behavior.recheck_auto_decisions_pct` và `trust_conditions` trong `world_patch.json` |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `____` · đo bằng gì `____` · bao nhiêu ở mốc base `____`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | | | |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | | | |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | | | |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | | | |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | | | |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | | | |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | | | |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | | | |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| Trưởng ca CSKH, Trần Thị Hạnh (`NV-HANH`), người đứng tên duyệt | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | **Cao**: khoản trên `auto_limit_vnd` 200.000đ (REFUND-v3) phải có một phê duyệt chị cấp **cho đúng ticket đó**, còn hạn, chưa thu hồi, `max_vnd` ≥ số tiền; chị đứng tên và phải giải trình với kiểm toán | **Không có**: `lab10/agent.py` bước 5 tra `lookup_approvals(order_id=...)` rồi `(customer_id=...)` và lấy luôn mã đầu tiên (`cands[0]`), không kiểm `ticket_id`, `status`, `expires_at`, `max_vnd`. Trace `S8-01@11` (base và after đều vậy): `approval_used {"approval_id": "A-2801"}` (mã của `T-OLD-2801`, `status: used`), rồi `issue_refund 230.000đ` ghi `approval_id: A-2801`. `S8-03@11`: dùng `A-2803` có `max_vnd` 150.000đ cho khoản 235.000đ. Cổng vòng 1 không kiểm mã duyệt | **Lệch** → gate trả quyền về cho NV-HANH: mã duyệt không hợp lệ thì `escalate` vào hàng chờ của chị, không tự chi |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | Khoản ≤ 200.000đ trợ lý tự chi, có ghi chú, nhân viên chỉ kiểm mẫu 10%. Khoản > 200.000đ chỉ chi khi mã duyệt khớp **đúng ticket**, `status` = valid, `expires_at` ≥ hôm nay, `max_vnd` ≥ số tiền, người duyệt NV-HANH; sai một điều thì chuyển chị Hạnh. Trong ngày **không còn khoản nào dùng mã không hợp lệ** | `operations.decision_note` = true, `review_sampling_pct` = 10, `approver_id` = NV-HANH (đã có từ vòng 1); thêm: ghi chú quyết định nêu rõ có dùng mã duyệt không và kết quả kiểm mã; chỉ số theo dõi số khoản dùng mã không hợp lệ mỗi ngày (phải = 0) | **Biết:** mỗi quyết định dựa vào đâu, mã duyệt nào, đã kiểm những gì; chị Hạnh giữ quyền với mọi khoản trên hạn mức. **Không cần** kiểm tay từng cái vì các khoản sai mã bị chặn trước khi chi |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | Trước kiểm toán, nhân viên CSKH để trợ lý tự chi cả những khoản trên 200.000đ có gắn mã duyệt, không kiểm lại (`recheck_auto_decisions_pct` 0 ở bộ nền): thấy dòng sổ cái có `approval_id` là coi như "chị Hạnh đã duyệt" | `ledger[].approval_id` trên dòng `issue_refund` (ví dụ `S8-01@11`: `A-2801`, 230.000đ); sự kiện `approval_used` chỉ ghi mã, không ghi mã đó của ticket nào, còn hạn không | **Biết:** khoản chi có mã duyệt. **Không biết:** mã đó cấp cho ticket khác (`A-2801` của `T-OLD-2801`, `A-2804` của `T-OLD-2808`), đã hết hạn (`A-2802` hết 2026-11-10), đã thu hồi (`A-2806`), hay hạn mức thấp hơn khoản chi (`A-2803` 150.000đ cho 235.000đ) |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | Chị Hạnh cấp mã duyệt cho từng ticket và tin rằng hệ thống chỉ dùng mã cho đúng ticket chị duyệt, trong hạn mức chị đặt, nên không xem lại sổ cái | Bảng `approvals` (`ticket_id`, `order_id`, `customer_id`, `max_vnd`, `expires_at`, `status`, `approver_id` = NV-HANH) trong `incidents/S8/world_patch.json`; agent tra theo `order_id` / `customer_id` chứ không theo `ticket_id` | **Biết:** mình đã cấp mã nào, cho ticket nào, tối đa bao nhiêu. **Không biết:** trợ lý tìm mã theo đơn hoặc theo khách rồi lấy mã đầu tiên, nên tên chị bị gắn vào khoản chị không duyệt |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | Sau kiểm toán ngày 16/11, cả ca được lệnh kiểm tay **mọi** quyết định, kể cả khoản 20.000đ (`S8-60@11` chỉ hoàn 16.000đ, không cần mã duyệt, vẫn bị kiểm lại). Hàng chờ 36 ca ùn, chờ lâu nhất 216 phút, chi phí 11.325đ/ticket > làm tay | `staff_behavior.recheck_auto_decisions_pct` = 100; ghi chú quyết định (`decision_note`, `S8-01@11` after) chỉ có `status`, `amount_vnd`, `basis`, `delay_days_used`, **`reason` để trống, không có mã duyệt và kết quả kiểm mã** | **Không biết:** quyết định nào an toàn (khoản nhỏ không cần duyệt) và quyết định nào có dùng mã duyệt, mã đó có hợp lệ không, nên phải tra lại từ đầu từng ca |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | Chị Hạnh bị kiểm toán ghi là người duyệt các khoản chị không duyệt, phải giải trình, nên rút niềm tin với toàn bộ hệ thống và hỏi "hệ thống lấy mã duyệt kiểu gì" | Report grade S8: "Niềm tin của nhân viên duyệt: **chưa đạt** · còn thiếu: trong ngày vẫn có khoản hoàn dùng phê duyệt không hợp lệ"; `ledger[].approval_id` của `S8-01`, `S8-02`, `S8-03`, `S8-04`, `S8-06` | **Biết:** có khoản đứng tên chị mà sai. **Không biết:** có bao nhiêu khoản như vậy, từ khi nào, và có cách nào chặn trước thay vì chỉ phát hiện ở kiểm toán |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | Khoản ≤ 200.000đ trợ lý tự chi, có ghi chú, nhân viên chỉ kiểm mẫu 10%. Khoản > 200.000đ chỉ chi khi mã duyệt khớp **đúng ticket**, `status` = valid, `expires_at` ≥ hôm nay, `max_vnd` ≥ số tiền, người duyệt NV-HANH; sai một điều thì chuyển chị Hạnh. Trong ngày **không còn khoản nào dùng mã không hợp lệ** | `operations.decision_note` = true, `review_sampling_pct` = 10, `approver_id` = NV-HANH (đã có từ vòng 1); thêm: ghi chú quyết định nêu rõ có dùng mã duyệt không và kết quả kiểm mã; chỉ số theo dõi số khoản dùng mã không hợp lệ mỗi ngày (phải = 0) | **Biết:** mỗi quyết định dựa vào đâu, mã duyệt nào, đã kiểm những gì; chị Hạnh giữ quyền với mọi khoản trên hạn mức. **Không cần** kiểm tay từng cái vì các khoản sai mã bị chặn trước khi chi |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `ledger[].approval_id` (gắn tên NV-HANH vào khoản chi mà không kiểm mã) và cách agent tra `approvals` theo `order_id`/`customer_id` rồi lấy `cands[0]`, không đối chiếu `ticket_id`, `status`, `expires_at`, `max_vnd`; cộng với ghi chú quyết định (`decision_note`) không nói gì về mã duyệt (`reason` trống).
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: **Thấy:** mỗi quyết định có ghi chú (`decision_note` = true), khoản trên hạn mức nêu mã duyệt đã dùng và mã đó khớp ticket, còn hạn, đủ hạn mức. **Giữ quyền:** NV-HANH (`approver_id`) là người duy nhất cho phép chi trên 200.000đ; mã không hợp lệ thì về hàng chờ của chị, trợ lý không tự chi. **Kiểm mẫu:** 10% quyết định tự động (`review_sampling_pct` = 10, đúng `trust_conditions.min_sampling_pct`), với điều kiện trong ngày không còn khoản nào dùng mã không hợp lệ; nếu còn thì quay lại kiểm 100% tới khi sạch. Ba con số này đã có trong `config/operating_gates.json` mục `operations` từ vòng 1; phần còn thiếu (chặn mã không hợp lệ) là cổng code của Kỹ sư cổng.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `________________`

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: Một lệnh `issue_refund` có số tiền vượt hạn mức tự động của chính sách đang hiệu lực (REFUND-v3: 200.000đ) chỉ được ghi khi có một phê duyệt của người duyệt đứng tên (NV-HANH) thoả đủ năm điều kiện: `status` = `valid` (không phải `used` hay `revoked`); `expires_at` không sớm hơn ngày hiện tại (`as_of` 2026-11-16); `ticket_id` của phê duyệt trùng ticket đang xử lý; `order_id` và `customer_id` khớp đơn đang hoàn; số tiền hoàn không vượt `max_vnd`. Thiếu một điều kiện thì không ghi sổ và chuyển người duyệt. Nếu spec này bị vi phạm thì trợ lý hoàn tiền trên mã duyệt không hợp lệ, trưởng ca bị đứng tên oan, và nhân viên không còn tin nên kiểm tay 100% quyết định.

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): `write_gate` nhánh `tool == "issue_refund"`, so `action["amount_vnd"]`, `ticket_id`, `order_id` với bảng `approvals` trong `world_patch.json` (ví dụ ứng với thẻ: A-2802 hết hạn 2026-11-10, A-2803 `max_vnd` 150.000đ thấp hơn khoản hoàn, A-2806 `revoked`, A-2801 gắn ticket khác `T-OLD-2801` và đã `used`; đối chứng hợp lệ A-2805 cho S8-05). Trên report `lab10.grade --incident S8`: dòng `wrongful_refund_vnd` (gói nhìn thấy, đang 6.845.000đ ở mốc prepared) phải về 0, và dòng "Niềm tin của nhân viên duyệt" chuyển từ "chưa đạt" sang "đạt".

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): Người thiết kế ngầm tin rằng **mã phê duyệt nào tìm thấy trong bảng `approvals` theo đơn hoặc theo khách thì cũng là phê duyệt của trưởng ca cho chính yêu cầu đang xử lý, và vẫn còn hiệu lực**. Tức là ngoài đời mỗi khách hay mỗi đơn chỉ có một yêu cầu bồi thường, mỗi mã duyệt chỉ được cấp cho đúng một ticket, và trạng thái của mã (đã dùng, hết hạn, bị thu hồi, hạn mức) luôn được người duyệt cập nhật kịp thời trước khi trợ lý tra tới. Đi kèm là giả định thứ hai: nhân viên CSKH sẽ tin quyết định tự động chỉ vì nó có gắn mã duyệt, nên không cần ghi chú giải thích.

Vì sao có thể sai:
- **Một khách, một đơn có nhiều yêu cầu theo thời gian.** C-08 có mã `A-2801` cấp cho yêu cầu cũ `T-OLD-2801` (đã `used`), và trợ lý dùng lại mã đó cho yêu cầu mới `S8-01` (`S8-01@11`: `approval_used A-2801`, chi 230.000đ). C-11 có `A-2804` cấp cho `T-OLD-2808` (đơn O-2808) nhưng trợ lý tìm theo khách và gắn nó vào đơn O-2804.
- **Mã duyệt có vòng đời ngoài phần mềm.** Trưởng ca cấp mã theo hạn (`A-2802` hết hạn 2026-11-10), thu hồi khi đổi ý (`A-2806` `revoked`), và đặt hạn mức theo từng ca (`A-2803` chỉ 150.000đ nhưng khoản chi 235.000đ). Ngoài đời việc thu hồi hay hết hạn thường được báo miệng hoặc cập nhật chậm, nên bảng `approvals` có thể còn mã "trông như hợp lệ".
- **Người đứng tên chịu trách nhiệm pháp lý, nên lòng tin của họ không tự có.** Theo `staff_behavior.trust_conditions` trong `incidents/S8/world_patch.json`, nhân viên chỉ thôi kiểm tay khi có ghi chú giải thích, kiểm mẫu ≥ 10%, người duyệt là NV-HANH và **trong ngày không còn khoản nào dùng phê duyệt không hợp lệ**. Chỉ một khoản sai là đủ để cả ca quay về kiểm 100% (`recheck_auto_decisions_pct` = 100), như tin nhắn của chị Hạnh ngày 16/11.

Hệ quả cần kiểm trong pilot thật: đo tỉ lệ ticket mà mã duyệt tìm được không khớp `ticket_id`, hết hạn hoặc bị thu hồi; và đo thời gian từ lúc trưởng ca thu hồi mã tới lúc bảng `approvals` cập nhật.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `__________`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: ______________________________ (cho ai: __________, đo bằng: __________)
 └─ HOẶC
 ├─ [1] ______________________________ tầng: đầu vào / data / hành động / quyền hạn / vận hành / kinh doanh
 │ └─ vì: ________________________ bằng chứng: ticket ______@seed ____
 ├─ [2] ______________________________ tầng: ______
 │ └─ vì: ________________________ bằng chứng: ticket ______@seed ____
 └─ [3] ______________________________ tầng: ______
 └─ vì: ________________________ bằng chứng: ______
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | | |
| [2] | | |
| [3] | | |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | | | | | |
| [2] | | | | | |
| [3] | | | | | |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | |
| **Bước / hành vi được đo** | |
| **Thước đo** (một câu, có đơn vị) | |
| **Dữ liệu** (trường nào của trial, không có nhãn) | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | |
| **Khung thời gian / ngưỡng báo động** | |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `__________`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] ______________________________
 └─ HOẶC
 ├─ [1] ______________ VÀ [gate ______ hỏng]
 ├─ [2] ______________ VÀ [gate ______ hỏng]
 └─ [3] ______________ (còn hở?)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | | | | |
| [2] | | | | |
| [3] | | | | |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| | | | |
| | | | |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp ___ lần trong một giờ thì: …
2. Nếu nhà cung cấp LLM lỗi quá ___ phút thì: …
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: …

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | phải giống v1 |
| Hash chốt cổng vòng 1 | phải giống v1 |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: ________ · prepared: ________ · after: ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | |
| Bằng chứng 2 | |
| Bằng chứng 3 | |
| Khớp dòng nào trong `decision_rule` đã ký? | |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: …
- Report tự kiểm tra: mã lần chạy `__________` · ô nào còn đỏ (nguyên nhân × tầng): …
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: …
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: …
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: …

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: …
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: …
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: …
