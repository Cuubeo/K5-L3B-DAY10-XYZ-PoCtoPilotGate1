# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):
- Lớp: `L3A` / `L3B`
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`
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
