# Đề tài 3: Triển khai Hệ thống Website Quảng bá Sản phẩm (WordPress)
- Môn học: Triển khai và Quản trị Hệ thống Phần mềm
- Sinh viên thực hiện: Trần Quốc Dũng

## 1. Cổng truy cập dịch vụ
- Website WordPress (HTTPS): https://192.168.230.129
- Quản trị phpMyAdmin: http://192.168.230.129:8081
- Giám sát Prometheus: http://192.168.230.129:9090
- Giám sát Grafana: http://192.168.230.129:3000 (User: admin / Pass: xem trong .env)

## 2. Các câu truy vấn LogQL
- Log Nginx: {container="nginx_proxy"}
- Log lỗi hệ thống: {job="docker"} |~ "(?i)(error|warn|fail|404|500)"
- Tốc độ sinh log: sum by (container) (rate({job="docker"}[1m]))

## 3. Biện pháp Hardening
- Network Isolation (Mạng backend cô lập DB)
- Phân quyền người dùng DB (wp_user)
- Mật khẩu mạnh lưu trữ trong .env
- SSL/TLS kèm các Security Headers trên Nginx
- Container chạy quyền Non-root và no-new-privileges
