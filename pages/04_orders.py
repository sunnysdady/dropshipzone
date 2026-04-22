import streamlit as st
import streamlit_antd_components as stc
import pandas as pd
import asyncio
from services.order_service import OrderService
from services.shipment_service import ShipmentService

def run():
    st.title("📦 订单管理")

    # ---- 拉取订单 ----
    order_svc = OrderService()
    with st.expander("过滤条件"):
        status = st.selectbox("状态", ["全部", "complete", "processing", "canceled"], index=0)
        date_from = st.date_input("开始日期", value=None)
        date_to   = st.date_input("结束日期", value=None)

        params = {}
        if status != "全部": params["status"] = status
        if date_from: params["purchase_date_from"] = str(date_from)
        if date_to:   params["purchase_date_to"]   = str(date_to)

    with st.spinner("加载订单…"):
        resp = asyncio.run(order_svc.list_orders(**params))
    if not resp["success"]:
        st.error(f"获取订单失败：{resp['error']}")
        return

    df_orders = pd.json_normalize(resp["data"]["orders"])
    st.subheader("订单列表")
    edited = st.data_editor(df_orders, num_rows="dynamic")

    # ---- 批量上传追踪号 ----
    uploaded = st.file_uploader("上传包含 order_id / tracking_number / carrier 的 CSV/Excel",
                               type=["csv","xlsx"])
    if uploaded:
        df_track = pd.read_excel(uploaded) if uploaded.name.endswith('.xlsx') else pd.read_csv(uploaded)
        required = {"order_id","tracking_number","carrier"}
        if not required.issubset(set(df_track.columns)):
            stc.toast(f"文件必须包含列：{', '.join(required)}", type="error")
        else:
            if stc.button("🚚 提交发货"):
                payload = [
                    {
                        "order_id": str(row["order_id"]),
                        "tracks": [{"carrier": row["carrier"], "tracking_number": str(row["tracking_number"])}],
                    }
                    for _, row in df_track.iterrows()
                ]
                with st.spinner("发送发货请求…"):
                    shipment_svc = ShipmentService()
                    result = asyncio.run(shipment_svc.create_shipments(payload))
                if result["success"]:
                    stc.toast("发货成功 🎉", type="success")
                else:
                    stc.toast(f"发货失败：{result['error']}", type="error")
