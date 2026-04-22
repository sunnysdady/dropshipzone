import streamlit as st
from utils.theme import load_css, toggle_dark_mode

# 页面基本配置
st.set_page_config(page_title="DSZ 运营面板", layout="wide")

# 注入 macOS 风格 CSS（有回退）
load_css()

# 暗黑模式开关
toggle_dark_mode()

# 简单导航
PAGES = {
    "📊 看板": "pages/01_dashboard.py",
    "🔎 爬取商品": "pages/02_scraper.py",
    "🛒 商品管理": "pages/03_products.py",
    "📦 订单管理": "pages/04_orders.py",
}

selection = st.sidebar.radio("🧭 请选择页面", list(PAGES.keys()))
module_path = PAGES[selection]

# 动态引入页面模块
module = __import__(module_path.replace("/", ".").replace(".py", ""), fromlist=["run"])
module.run()
