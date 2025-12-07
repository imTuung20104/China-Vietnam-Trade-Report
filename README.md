# 🇨🇳 China-Vietnam Trade Dashboard

> **Bảng điều khiển theo dõi kim ngạch Xuất Nhập Khẩu (Interactive Dashboard).**

![Streamlit](https://img.shields.io/badge/App-Streamlit-FF4B4B) ![Data](https://img.shields.io/badge/Data-Vietnam_Customs-yellow)

## 📸 Giao diện Dashboard
Dưới đây là biểu đồ theo dõi xu hướng nhập khẩu theo thời gian thực:

<img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop" width="100%" style="border-radius: 10px">

## 📊 Tính năng chính
1.  **Theo dõi xu hướng:** Biểu đồ đường (Line Chart) thể hiện kim ngạch nhập khẩu tăng/giảm qua các tháng.
2.  **Top Hàng hóa:** Biểu đồ cột (Bar Chart) top 5 mặt hàng nhập nhiều nhất từ Trung Quốc.
3.  **Cảnh báo tỷ giá:** Theo dõi biến động CNY/VND để chọn thời điểm thanh toán T/T tốt nhất.

## 📂 Dữ liệu
Dữ liệu được lấy từ báo cáo định kỳ của **Tổng cục Hải quan Việt Nam**, sau đó được làm sạch bằng **Pandas**.
