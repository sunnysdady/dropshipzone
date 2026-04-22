import streamlit as st
import pandas as pd

def run():
    st.title("🛒 商品管理（示例）")
    st.write("以下数据为示例，实际场景请对接 DSZ API 获取真实数据。")

    df = pd.DataFrame({
        "sku": ["SKU001", "SKU002", "SKU003"],
        "name": ["商品A", "商品B", "商品C"],
        "stock": [10, 0, 25],
        "price": [9.99, 19.99, 29.99],
        "status": ["启用", "禁用", "启用"]
    })
    st.dataframe(df)
