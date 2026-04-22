import streamlit as st
import streamlit_antd_components as stc
import pandas as pd
import asyncio
from scraper.product_scraper import fetch_product
from services.product_service import ProductService

def run():
    st.title("🔎 1688 商品抓取（Selenium）")

    url = stc.input(
        label="商品链接（1688）",
        placeholder="https://detail.1688.com/offer/xxxxxx.html",
        key="url_input",
    )
    if stc.button("🚀 开始抓取", key="scrape_btn"):
        if not url:
            stc.toast("请先填写链接", type="error")
        else:
            with st.spinner("正在加载页面…"):
                try:
                    data = fetch_product(url)
                    st.success("抓取成功 🎉")
                    st.json(data)

                    # 把抓取结果转换为 DataFrame，便于编辑
                    df = pd.json_normalize(data)
                    edited = st.data_editor(df, num_rows="dynamic")
                    if stc.button("✅ 上架到 DSZ", key="upload_btn"):
                        products = edited.to_dict(orient="records")
                        svc = ProductService()
                        result = asyncio.run(svc.batch_add(products))
                        stc.toast("已提交上架请求", type="success")
                except Exception as e:
                    stc.toast(f"抓取失败：{e}", type="error")
