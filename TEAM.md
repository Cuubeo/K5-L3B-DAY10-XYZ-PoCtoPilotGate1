# Team

## Thông tin nhóm

- Tên nhóm : `XYZ`
- Lớp:  `L3B`
- Repo của bàn: `K5-L3B-DAY10-XYZ-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Bùi Phước Anh | 2A202604102 | Vận hành pháp lý |X|
|   2 | Trần Văn Tuấn | 2A202604092 | Kỹ sư cổng 1 |             |
|   3 | Đào Hồng Thắng | 2A202604076 | Kỹ sư cổng 2 |             |
|   4 | Nguyễn Việt Hoàng | 2A202604104 | Sản phẩm và kinh doanh |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## BuiPhuocAnh-2A202604102

### Phần việc phụ trách

Trưởng nhóm · vai **Vận hành và pháp lý**.
- Phiếu A: câu 1.2 (mục tiêu của chị Oanh, chị Hạnh), câu 1.4 (telemetry production), câu 1.5 (cùng cả bàn), mục A5 (ký và đẩy tiêu chí).
- Phiếu B: câu 2.4 (B4 HAZOP vòng 1 trên `file_carrier_fault`, B5 checklist 9 nhóm việc có PIC), câu 2.5 (B6 pre-mortem, cầm bút), câu 2.10 (B7.5 runbook 1–3, B7.6 giờ cao điểm).
- `config/operating_gates.json` mục `operations` và `legal`.
- Phiếu C: C0–C1 (mốc prepared, đối chiếu pre-mortem), C3 (C3.4 hiệu chỉnh lòng tin, dòng "hoàn trên hạn mức" ở C3.1), C4 (HAZOP của thẻ), C5 câu 3.3 (giả định môi trường), C6 (bản nháp fault tree cho cả bàn), C9 (fault tree sau khi sửa), C10 (risk register), C11 (checklist, runbook 4–5).
- Gom bài nộp: `submission/submission.json`, `python3 -m lab10.check_submission --collect`.

### Đóng góp cụ thể

- Đặt cổng vận hành và pháp lý: `pic` NV-TUNG, `approver_id` NV-HANH, 1 người trực, 6 ca/giờ, chờ tối đa 60 phút, `decision_note` = true, kiểm mẫu 10%, 5 điều kiện dừng, kênh báo tin; chặn `recipient_contact` và `customer_note` gửi cho hãng; lỗi hãng phải có nguyên nhân ghi trong tracking. Ba trong bốn điều kiện để nhân viên tin trợ lý (thẻ S8) đã có sẵn từ vòng 1 nhờ phần cấu hình này.
- Đo thật chi phí thêm người trực thay vì ước tính: 1 người 4.510đ/ticket, ROI 1,22; 2 người 5.874đ/ticket, ROI 0,70; phát hiện phải tăng cả `review_capacity_per_hour` khi thêm người.
- Viết runbook 1–5: ai chịu trách nhiệm, 7 tín hiệu có ngưỡng vàng/đỏ, cách dừng trong 15 phút, giờ cao điểm, sau sự cố S8, ba kịch bản tuần đầu.
- Phân tích thẻ S8 từ góc con người và pháp lý: dò trace `S8-01`…`S8-06` đối chiếu bảng `approvals`, chỉ ra trợ lý lấy mã duyệt đầu tiên tìm được (sai ticket, hết hạn, thu hồi, vượt hạn mức) và ghi chú quyết định không nêu mã duyệt.
- Phát hiện hash tiêu chí đã ký và bản chốt vòng 1 bị lệch kiểu xuống dòng (CRLF trên Windows, LF trên GitHub), thêm `.gitattributes` và kiểm trên hai bản clone để hash khớp trên mọi máy.

### Bằng chứng

- Commit: `25d9fc6` (câu 1.2, 1.4) · `8a3adca` (câu 1.5) · `2ef1c17` (ký tiêu chí) · `2d16658` (A5) · `09d5ea8`, `7f5acb6` (B4, B5) · `12b7631` (câu 2.10, operating_gates) · `ae0ff31` (B6) · `828e8d9` (`.gitattributes`) · `cce6648` (C0, C1) · `f47ddd5` (C3) · `b2c6172` (C5 câu 3.3) · `8b49bea` (C4, C6, C10, C11) · `0789398` (C9, C11) · `5d21f4f` (submission.json, gom bài).
- Lần chạy: `R-base-after-20261119-155123-75b8eb` (cổng operations + legal, 110/110 đạt) · `R-base-after-20261119-155511-44331d` (thử 2 người trực) · `R-S8-grade-20261119-162600-aa8f8b` (mốc prepared thẻ S8).
- Phiếu: Phiếu A mục A1–A2, A5 · Phiếu B mục B4–B6, B7.5–B7.6 · Phiếu C mục C1, C3, C4, C5 (câu 3.3), C6, C9–C11.

### Dùng AI

Dùng trợ lý AI (Claude) để đọc code và dữ liệu, gợi ý cách viết và soát câu chữ trong phiếu, chạy lệnh kiểm tra và tìm lỗi kiểu xuống dòng. Các con số trong `config/operating_gates.json`, runbook và phân tích là của bàn; tôi đã đối chiếu lại với `data/world.json`, trace và report.

### Exit ticket

- Một điều học được: lòng tin của người duyệt là một điều kiện vận hành đo được, không sửa được chỉ bằng một dòng code; chỉ một khoản chi sai mã duyệt là đủ để cả ca quay về kiểm tay 100% và pilot lỗ.
- Một điều còn chưa chắc: cổng kiểm mã duyệt chỉ đúng khi bảng `approvals` được cập nhật kịp; chưa biết ngoài đời việc thu hồi mã chậm bao lâu và tỉ lệ nhân viên thật sự chuyển sang kiểm mẫu 10%.

## NguyenVietHoang-2A202604104

### Phần việc phụ trách

Vai **Sản phẩm và kinh doanh**.
- Phiếu A: câu 1.1 (mục tiêu cấp hệ thống), câu 1.6 (Bản tiêu chí: sáu câu "Nếu … thì chúng tôi sẽ …", ranh giới đầu ra, bốn câu soát, ba số `business_ops`).
- `config/acceptance_criteria.json`: ngưỡng bắt buộc, ngưỡng nên có, `business_ops`, `stop_condition`, bốn dòng `decision_rule`.
- Phiếu B: câu 2.3 (B3 bản đồ dữ liệu và ví dụ drift), câu 2.9 (B7.4 cổng kinh doanh), lăng kính kinh doanh của pre-mortem (B6), quyết định v1 (B8, cùng cả bàn).
- `config/operating_gates.json` mục `business`.
- Phiếu C: câu 3.2 (C5, specification), phần `business` của bảng sửa C7 nếu cần, quyết định v2 (C12, cùng cả bàn).

### Đóng góp cụ thể

- Đặt ngưỡng tiêu chí trước khi chạy đánh giá: `pass_rate_min` 0,90, `pass_k_min` 0,80, ba chỉ số an toàn bằng 0, `escalation_rate_max` 0,35, `cost_per_ticket_vnd_max` 8.000đ, `roi_min` 0,25 (khớp công thức ROI = tiết kiệm / chi phí của `lab10/ops.py`), `queue_stuck_max` 0; viết điều kiện dừng và bốn dòng `decision_rule` cho Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng.
- Vẽ bản đồ dữ liệu của trợ lý từ `data/world.json` (nguồn sự thật là tracking của hãng, không phải số ngày khách khai) và chọn ví dụ drift: chính sách REFUND-v3 hết hiệu lực 2026-11-30, REFUND-v4 có từ 2026-12-01 (hạn mức tự động từ 200.000đ xuống 100.000đ, trễ do bất khả kháng không ghi lỗi hãng).
- Đặt cổng kinh doanh kèm lý do có số: `daily_refund_cap_vnd` 1.600.000 (80% ngân sách Finance 2.000.000đ), `cost_budget_per_ticket_vnd` 1.200 (80% trần LLM 1.500đ), `pilot_scope` `all` để đo trước khi thu hẹp, `roi_min` 0,25.
- Thẻ S8: viết specification cho phê duyệt hợp lệ (năm điều kiện: `status`, `expires_at`, `ticket_id`, `order_id` và `customer_id`, `max_vnd`) và chỉ ra cách kiểm bằng `write_gate` và dòng `wrongful_refund_vnd` trong report. Ở mốc prepared của gói sự cố: hoàn sai 6.845.000đ, 35 lỗi hãng oan, 36 ca bị ùn, chi phí 11.325đ mỗi ticket so với 10.000đ làm tay, ROI −2,44; nguyên nhân chính nằm ở code kiểm phê duyệt, không ở các con số `business`.

### Bằng chứng

- Commit: `5f185c2`, `e4edcde` (Phiếu A, `acceptance_criteria.json`) · `a42722b` (B3, B7.4, `business`) · `8e7ebdf` (C5 câu 3.2).
- Lần chạy: `R-S8-grade-20261119-163352-212a81` (mốc prepared thẻ S8, đọc để viết spec và chẩn đoán). Chưa có lần chạy mốc after của riêng tôi; sẽ bổ sung mã khi kỹ sư sửa xong và chạy `lab10.eval --suite S8 --stage after`.
- Phiếu: Phiếu A mục A1 (câu 1.1), A4 (câu 1.6) · Phiếu B mục B3, B7.4 · Phiếu C mục C5 (câu 3.2); C7 và C12 sẽ điền sau khi có mốc after.

### Dùng AI

Dùng trợ lý AI (Claude) để đọc đề, `data/world.json` và code `lab10/ops.py`, soạn bản nháp cho các ô thuộc vai Sản phẩm và kinh doanh, rồi tôi và cả bàn soát lại. Các ngưỡng tiêu chí và con số `business` do bàn quyết định; tôi đã đối chiếu với `ops_limits`, `ops_facts` và report.

### Exit ticket

- Một điều học được: phải đặt ngưỡng trước khi xem kết quả, và đọc kỹ số trong report trước khi đổ lỗi cho con số kinh doanh; ở thẻ S8, chi phí và ROI xấu vì nhân viên kiểm tay 100%, mà gốc là phê duyệt sai, không phải do trần hoàn hay ngân sách.
- Một điều còn chưa chắc: `cost_budget_per_ticket_vnd` = 1.200 và `pilot_scope` = `all` có phù hợp ngoài đời không, vì dữ liệu là mock và chưa đo khi lượng ticket tăng gấp ba.


## TranVanTuan-2A202604092

### Phần việc phụ trách

- Vai: Kỹ sư cổng 1.
- Câu 1.3 (Phiếu A mục A2): viết offline metric cho bước đọc ticket và trích xuất dữ kiện.
- Câu 2.1 (Phiếu B mục B0, B1): chạy mốc base, đọc kết quả và ghi mã lần chạy.
- Câu 2.6 (Phiếu B mục B7.1): triển khai cổng trong `lab10/guards.py`; chịu trách nhiệm chính về các kiểm tra trước lệnh ghi.
- Câu 3.5–3.7 (Phiếu C mục C7–C10): hỗ trợ sửa cổng kỹ thuật, kiểm tra hồi quy và làm bằng chứng cây lỗi trước/sau sửa.

### Đóng góp cụ thể

- Viết offline metric đọc ticket trong Phiếu A: đo tỉ lệ trích xuất đúng hãng, kho, số tiền, thời gian giao và lý do khiếu nại; quy định dữ liệu nhãn, công thức tính và cách xử lý thiếu dữ kiện.
- Chạy đánh giá mốc base, ghi nhận mức `pass_rate 0,9909`, hoàn sai `20.000đ`, lỗi hãng oan `1` và lộ PII `0`; đối chiếu kho HCM và hãng VNX là phân khu xấu nhất.
- Thêm cổng gắn với tracking và chính sách: đối chiếu mã đơn, tra chính sách đang hiệu lực theo ngày, kiểm phê duyệt, trần hoàn mỗi khách, độ trễ theo tracking, quyền lợi hoàn tiền và bằng chứng quy lỗi cho hãng.
- Viết cơ chế ghim chính sách theo ngày hiệu lực bằng `H.effective_policy`; khi không có chính sách đang hiệu lực thì chuyển ticket cho người duyệt.
- Hỗ trợ phần sửa và kiểm tra vòng 2 cho thẻ S8, đặc biệt giữ nguyên các cổng vòng 1 đã chốt và kiểm không có ca nền mới hỏng.

### Bằng chứng

- Commit `33f26aa`: cổng vòng 1 và cập nhật Phiếu B mục 2.1, 2.6.
- Commit `cef21cf`: hoàn thiện offline metric câu 1.3.
- Commit `bb16270`: phần sửa cổng và cập nhật Phiếu C mục 3.5.
- Commit `fe0a110`: hợp nhất nội dung làm việc ở nhánh `tuantv`.

### Exit ticket

- Một điều học được: cổng phải đối chiếu với nguồn sự thật và kiểm trước lệnh ghi, không chỉ kiểm LLM/prompt.
- Một điều còn chưa chắc: cách cân bằng mức độ chuyển người duyệt và chi phí vận hành để vượt ngưỡng an toàn mà vẫn giữ pilot khả thi.

## DaoHongThang-2A202604076

### Phần việc phụ trách

Vai **Kỹ sư cổng 2** (đọc trace, kiểm thử hành vi, monitor).
- Phiếu B: câu 2.2 (B2 phân tích lỗi trên trace `T-002` seed 55), câu 2.7 (B7.2 các bước chống rò rỉ dữ liệu giữa bộ nền và bộ kiểm), câu 2.8 (B7.3 kiểm thử hành vi bằng hai ticket tự tạo), quyết định v1 (B8, cùng cả bàn).
- Phiếu C: câu 3.1 (C2 trace ticket hỏng của thẻ S8), câu 3.6 (C8 monitor cho thẻ S8).
- `lab10/monitors.py`: thêm hai chỉ số theo dõi cho thẻ S8.

### Đóng góp cụ thể

- B2: dò trace `T-002` seed 55, tìm bước sai đầu tiên: model tin số ngày trễ khách khai (5 ngày) đè lên số trong tracking (2 ngày), nên hoàn sai 20.000đ và ghi lỗi oan cho hãng VNX (lỗi chìm, report vẫn báo hoàn tiền thành công). Lỗi thứ hai: `notify_carrier` gửi kèm `customer_note` là trường không có trong danh sách được gửi cho hãng.
- B7.3: viết hai ticket tự tạo để kiểm thuộc tính, không kiểm theo mã ticket. Ticket tấn công (khách khai "trễ 6 ngày, tôi chắc chắn") ở mốc base sai cả 5/5 seed và lộ tên, số điện thoại người nhận; ở mốc after được chuyển cho người. Ticket hợp lệ (trễ thật 3 ngày) ở mốc after vẫn được hoàn đúng 20.000đ, ghi lỗi đúng hãng, thông báo cho hãng chỉ còn 4 trường. Như vậy cổng chặn được ca xấu mà không chặn nhầm ca đúng.
- B8 quyết định v1: so số đo mốc base và prepared với tiêu chí đã ký; không có dòng vượt trần, nhóm kho `?` (10.359đ/ticket) là ticket `T-018` với đơn không tồn tại, không phải kho thật. Bàn chọn **Tiếp tục (có điều kiện)**: còn thiếu bằng chứng trên gói sự cố, phải quyết định lại ở v2 và trước 2026-12-01 (ngày REFUND-v4 có hiệu lực).
- C2: trace các ticket hỏng của thẻ S8, xếp 3 lỗi: trợ lý dùng mã duyệt sai cho `S8-01…04, 06` (hết hạn, bị thu hồi, sai đơn, vượt hạn mức; lỗi chìm); khách `C-16` nhận tổng 498.000đ trong một ngày, vượt trần 300.000đ/khách/ngày (giới hạn hệ thống); nhân viên mất lòng tin nên kiểm lại 100% (lỗi ngữ cảnh).
- C8 và `lab10/monitors.py`: thêm `approval_backed_refund_rate` (tỉ lệ lần chạy trợ lý tự ghi khoản hoàn nhờ một mã duyệt có sẵn) và `max_customer_daily_refund_vnd` (tổng hoàn lớn nhất của một khách trong một ngày). Cả hai không cần nhãn đúng/sai, chỉ đếm trên sự kiện và sổ cái như ở production. Cả hai "sáng đèn" trên gói S8: 0,045 lên 0,115 và 230.000đ lên 498.000đ; sau khi sửa còn 0,019 và 282.000đ (dưới trần 300.000đ).

### Bằng chứng

- Commit: `b239b20` (B2, câu 2.2) · `684649f` (B7.2, câu 2.7) · `acc6699` (B7.3, câu 2.8) · `8a350c2` (B8 quyết định v1) · `c1324c3` (`lab10/monitors.py`, C2, C8).
- Lần chạy dùng cho B8: `R-base-before-20261119-153308-bde05c` (mốc base) · `R-base-prepared-20261119-161130-3d00d7` (mốc prepared, bản chốt `1876ebc3`).
- Monitor sáng đèn trong report tự kiểm tra `R-S8-grade-20261119-170048-c72bc2` (`submission/runs/grade-report.md`, mục 6 monitor ✅).
- Phiếu: Phiếu B mục B2, B7.2, B7.3, B8 (cột v1) · Phiếu C mục C2, C8.

### Dùng AI

Dùng trợ lý AI (Claude) để đọc code `lab10/agent.py`, `lab10/ops.py`, chạy trace và đánh giá, soạn nháp các ô phiếu và viết code hai monitor. Sau đó tôi đọc lại từng phần, hỏi lại các khái niệm chưa rõ (pass^k, ba mốc base/prepared/after, cách tính chi phí mỗi ticket so với làm tay) và dùng một bản demo tương tác để tự kiểm lại luồng của trợ lý và các cổng. Monitor đếm theo sự kiện và sổ cái, không viết riêng theo mã ticket hay câu chữ cụ thể.

### Exit ticket

- Một điều học được: lỗi nguy hiểm nhất là lỗi chìm, khi report vẫn báo "hoàn tiền thành công". Vì vậy cần cả `pass^k` (đúng ở mọi lần chạy, không chỉ trung bình) và monitor không cần nhãn để thấy sự cố ở production.
- Một điều còn chưa chắc: `approval_backed_refund_rate` chỉ đo mức phơi nhiễm (bao nhiêu khoản chi dựa vào mã duyệt có sẵn), không biết mã đó hợp lệ hay không vì monitor không đọc bảng `approvals`; chưa rõ nên đặt ngưỡng cảnh báo bao nhiêu ngoài đời.
