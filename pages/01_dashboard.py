import streamlit as st
import pandas as pd
import numpy as np

def run():
    st.title("📊 运营看板")
    st.write("这是一个最小化的看板，用于展示核心数据结构。请在实际环境中替换成真实数据源。")

    # 模拟数据（可替换成自定义 API 调用）
    data = {
        "指标": ["总订单数", "已发货", "待处理", "总收入"],
        "数值": [120, 95, 25, 25840]
    }
    df = pd.DataFrame(data)
    st.table(df)

    # 最近订单（示意）
    recent = pd.DataFrame({
        "order_id": [f"DSZ-{i:04d}" for i in range(1, 6)],
        "status": ["complete", "processing", "canceled", "complete", "processing"],
        "amount": [120.5, 89.0, 15.0, 60.0, 75.2],
        "date": pd.date_range(end=pd.Timestamp.today(), periods=5).to_pydatetime().tolist()
    })
    st.subheader("最近订单")
    st.dataframe(recent)
