import streamlit as st
import pandas as pd

def run():
    st.title("📦 订单管理（示例）")
    st.write("演示数据，实际请接入 DSZ 的订单 API。")

    df = pd.DataFrame({
        "order_id": ["DSZ-0001", "DSZ-0002", "DSZ-0003"],
        "status": ["processing", "complete", "processing"],
        "amount": [99.0, 49.5, 120.0],
        "date": pd.date_range(end=pd.Timestamp.today(), periods=3).to_pydatetime().tolist()
    })
    st.dataframe(df)

    st.subheader("批量发货（模拟）")
    uploaded = st.file_uploader("上传包含 order_id / tracking_number / carrier 的 CSV/Excel", type=["csv","xlsx"])
    if uploaded:
        st.success("模拟：已接收发货数据。请在真实环境中实现后端提交。")
