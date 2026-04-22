import streamlit as st
import streamlit_antd_components as stc
import pandas as pd
import asyncio
from services.product_service import ProductService

def run():
    st.title("🛒 商品管理")

    svc = ProductService()

    # ---- 拉取商品列表（带过滤） ----
    with st.expander("🔎 筛选查询"):
        name = st.text_input("商品名称（模糊）")
        sku = st.text_input("SKU")
        status = st.selectbox("状态", options=["全部", "启用", "禁用"], index=0)

        params = {}
        if name: params["name"] = name
        if sku:  params["skus"] = sku
        if status != "全部":
            params["status"] = "1" if status == "启用" else "0"

        with st.spinner("加载商品…"):
            resp = asyncio.run(svc.list_all(**params))
        if not resp["success"]:
            st.error(f"获取商品失败：{resp['error']}")
            return

    df = pd.json_normalize(resp["data"]["products"])
    edited = st.data_editor(df, num_rows="dynamic")

    # ---- 库存批量更新 ----
    if stc.button("🔄 批量更新库存", key="stock_btn"):
        stock_updates = [
            {"sku": row["sku"], "stock": int(row["stock"])}
            for _, row in edited.iterrows()
            if pd.notna(row["stock"])
        ]
        if stock_updates:
            with st.spinner("更新库存…"):
                result = asyncio.run(svc.batch_update_stock(stock_updates))
            st.success("库存更新请求已提交")
        else:
            st.warning("未检测到库存变更")

    # ---- 状态批量更新 ----
    if stc.button("🔁 批量更新状态", key="status_btn"):
        status_updates = [
            {"sku": row["sku"], "status": int(row["status"])}
            for _, row in edited.iterrows()
            if pd.notna(row["status"])
        ]
        if status_updates:
            with st.spinner("更新状态…"):
                result = asyncio.run(svc.batch_update_status(status_updates))
            st.success("状态更新请求已提交")
        else:
            st.warning("未检测到状态变更")
