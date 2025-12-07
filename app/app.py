# File: app/app.py
import streamlit as st
import pandas as pd
from charts import plot_import_trend # <-- Import hàm vẽ biểu đồ từ file charts.py của bạn

# 1. Cấu hình trang
st.set_page_config(page_title="Vietnam-China Trade Dashboard", layout="wide")

st.title("🇨🇳 Vietnam - China Trade Dashboard")
st.markdown("Theo dõi kim ngạch xuất nhập khẩu song phương.")

# 2. Giả lập dữ liệu (Data Mockup) cho giống thật
# Trong thực tế, đoạn này sẽ là pd.read_csv('dataset/vn_cn_trade_2024.csv')
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    'Import_Value_USD': [12000, 11500, 13000, 12500, 14000, 13800, 15000, 16000, 15500, 17000]
}
df = pd.DataFrame(data)

# 3. Hiển thị Dashboard
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Xu hướng Nhập khẩu (Import Trend)")
    # GỌI HÀM VẼ BIỂU ĐỒ CỦA BẠN Ở ĐÂY
    fig = plot_import_trend(df) 
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Thống kê nhanh")
    st.metric(label="Tổng kim ngạch (YTD)", value="$140.3B", delta="12%")
    st.metric(label="Tháng cao nhất", value="Oct 2024")
