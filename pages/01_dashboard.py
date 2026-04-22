import streamlit as st
import asyncio
import pandas as pd
from services.order_service import OrderService
from services.product_service import ProductService

def run():
    st.title("📊 运营看板")

    # ---- 订单概览 ----
    order_svc = OrderService()
    with st.spinner("加载订单数据…"):
        orders_resp = asyncio.run(order_svc.list_orders(limit=100))
    if orders_resp["success"]:
        df_orders = pd.json_normalize(orders_resp["data"]["orders"])
        st.subheader("最近订单")
        st.dataframe(df_orders[['order_id','status','grand_total','created_at']])
    else:
        st.error(f"获取订单失败：{orders_resp['error']}")

    # ---- 商品库存概览 ----
    prod_svc = ProductService()
    with st.spinner("加载库存数据…"):
        prod_resp = asyncio.run(prod_svc.list_all(limit=200, status=1))
    if prod_resp["success"]:
        df_prod = pd.json_normalize(prod_resp["data"]["products"])
        st.subheader("商品库存")
        st.dataframe(df_prod[['sku','name','stock','price']])
    else:
        st.error(f"获取商品失败：{prod_resp['error']}")
