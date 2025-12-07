# 🇨🇳 China-Vietnam Trade Dashboard

> **Bảng điều khiển tương tác theo dõi kim ngạch Xuất Nhập Khẩu Việt - Trung (Interactive Data App).**

[![Streamlit](https://img.shields.io/badge/App-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Viz-Plotly-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/)
[![Data Source](https://img.shields.io/badge/Data-Vietnam_Customs-yellow?style=flat-square)]()

## 🚩 Bối cảnh (Context)
Thị trường Trung Quốc biến động liên tục. Việc đọc các file PDF báo cáo từ Tổng cục Hải quan (General Dept of Vietnam Customs) rất khó để nhìn ra xu hướng (Trend) nhập hàng.
* **Mục tiêu:** Xây dựng dashboard giúp bộ phận Purchasing quyết định thời điểm nhập hàng tốt nhất.

## 📊 Tính năng Dashboard
1.  **Trend Tracker:** Biểu đồ đường (Line Chart) theo dõi biến động kim ngạch theo tháng (MoM).
2.  **Top Commodities:** Biểu đồ cột (Bar Chart) top 5 nhóm hàng nhập khẩu nhiều nhất (theo mã HS 2 số).
3.  **Exchange Rate Monitor:** Theo dõi biến động tỷ giá CNY/VND ảnh hưởng đến giá vốn hàng bán (COGS).

## 📂 Project Structure
```text
China-Vietnam-Trade-Report/
├── 📂 dataset/
│   ├── vn_cn_trade_2024.csv  # Dữ liệu sạch (Cleaned Data)
│   └── raw_customs_data/     # Dữ liệu thô tải từ HQVN
├── 📂 app/
│   ├── app.py                # File chạy Streamlit
│   └── charts.py             # Code vẽ biểu đồ Plotly
├── requirements.txt
└── README.md
