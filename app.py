import streamlit as st
from utils.theme import load_css, toggle_dark_mode

# ---------- 页面基本配置 ----------
st.set_page_config(page_title="DSZ 运营面板", layout="wide")
load_css()          # 注入 macOS UI（浅色）CSS
toggle_dark_mode()  # Sidebar 暗黑模式开关

# ---------- 页面路由 ----------
pages = {
    "📊 看板": "pages/01_dashboard.py",
    "🔎 爬取商品": "pages/02_scraper.py",
    "🛒 商品管理": "pages/03_products.py",
    "📦 订单管理": "pages/04_orders.py",
}
selection = st.sidebar.radio("🧭 请选择页面", list(pages.keys()))
module_path = pages[selection]
module = __import__(module_path.replace("/", ".").replace(".py", ""), fromlist=["run"])
module.run()
