import plotly.express as px

def plot_import_trend(df):
    """
    Vẽ biểu đồ đường thể hiện xu hướng nhập khẩu theo tháng
    Input: DataFrame chứa cột 'Month' và 'Import_Value_USD'
    """
    fig = px.line(df, 
                  x='Month', 
                  y='Import_Value_USD', 
                  title='Biến động Kim ngạch Nhập khẩu từ TQ (2024)',
                  markers=True)
    
    fig.update_layout(xaxis_title='Tháng', yaxis_title='Giá trị (USD)')
    return fig
