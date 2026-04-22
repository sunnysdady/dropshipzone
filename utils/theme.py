import streamlit as st
from pathlib import Path
import logging

# 绝对路径定位：确保云端也能正确找到 assets
base_dir = Path(__file__).resolve().parents[2]
MACOS_CSS = base_dir / "assets" / "macos.css"
DARK_CSS = base_dir / "assets" / "dark.css"

# 日志
logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def load_css():
    """注入 macOS 浅色主题 CSS；无文件时回退并告警"""
    css = ""
    try:
        css = MACOS_CSS.read_text(encoding="utf-8")
        logger.info(f"Loaded macOS CSS from {MACOS_CSS}")
    except FileNotFoundError:
        css = """
        /* 回退样式：确保页面可用 */
        .stButton > button { border-radius: 8px !important; }
        [data-testid="stAppViewContainer"] {
            font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        """
        logger.warning(f"macOS CSS not found at {MACOS_CSS}. Using fallback styles.")
    except Exception as e:
        logger.error(f"Error loading macos.css: {e}")
        css = """
        .stButton > button { border-radius: 8px !important; }
        """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def toggle_dark_mode():
    """在侧边栏提供暗黑模式开关并注入 dark.css（若开启）"""
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    st.sidebar.checkbox("🌙 暗黑模式", key="dark_mode")

    if st.session_state.dark_mode:
        css_dark = ""
        try:
            css_dark = DARK_CSS.read_text(encoding="utf-8")
            logger.info(f"Loaded dark CSS from {DARK_CSS}")
        except FileNotFoundError:
            logger.warning(f"dark.css not found at {DARK_CSS}. Dark mode may not be fully functional.")
        except Exception as e:
            logger.error(f"Error loading dark.css: {e}")
        if css_dark:
            st.markdown(f"<style>{css_dark}</style>", unsafe_allow_html=True)
