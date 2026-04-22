# utils/theme.py
import streamlit as st
from pathlib import Path

# 绝对路径定位 assets/macos.css，避免部署环境的工作目录变化问题
def load_css():
    base_dir = Path(__file__).resolve().parents[2]  # project root/dsz_tool
    macos_css_path = base_dir / "assets" / "macos.css"

    css_text = ""
    try:
        css_text = macos_css_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        # 回退样式，避免应用直接报错
        css_text = """
        /* 回退样式：确保页面可用但不美观到极致 */
        .stButton > button { border-radius: 8px !important; }
        [data-testid="stAppViewContainer"] { font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif; }
        """
        # 给出日志/提示，方便你知道需要提交 css 文件
        try:
            import logging
            logging.getLogger(__name__).warning(
                "macos.css 未找到，使用回退样式。请确保 assets/macos.css 已提交到仓库。"
            )
        except Exception:
            pass
    st.markdown(f"<style>{css_text}</style>", unsafe_allow_html=True)
