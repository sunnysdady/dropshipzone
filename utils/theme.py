# utils/theme.py

import streamlit as st
from pathlib import Path
import logging # 导入 logging 模块，用于在无法找到文件时打印警告

# 获取当前文件所在目录的上层目录的上一层目录（项目根目录）
# 这样可以更稳定地找到 assets 目录，无论 Streamlit Cloud 的工作目录如何变化
base_dir = Path(__file__).resolve().parents[2]
macos_css_path = base_dir / "assets" / "macos.css"
dark_css_path = base_dir / "assets" / "dark.css"

# 配置一个简单的 logger，用于输出警告信息
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_css():
    """
    一次性注入 macOS 浅色主题 CSS。
    如果文件找不到，则加载一个简单的回退样式，并打印警告。
    """
    css_text = ""
    try:
        # 尝试读取 macos.css 文件
        css_text = macos_css_path.read_text(encoding="utf-8")
        logger.info(f"Successfully loaded macOS CSS from: {macos_css_path}")
    except FileNotFoundError:
        # 如果文件不存在，使用回退样式
        css_text = """
        /* Fallback CSS: Ensures the app is functional but less styled */
        .stButton > button { border-radius: 8px !important; }
        [data-testid="stAppViewContainer"] { font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif; }
        """
        logger.warning(
            f"macOS.css not found at {macos_css_path}. Using fallback styles. "
            "Please ensure assets/macos.css is committed to your Git repository."
        )
    except Exception as e:
        # 捕获其他可能的读取文件错误
        logger.error(f"Error reading macOS.css: {e}")
        css_text = """
        /* Generic fallback in case of other read errors */
        .stButton > button { border-radius: 8px !important; }
        [data-testid="stAppViewContainer"] { font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif; }
        """

    st.markdown(f"<style>{css_text}</style>", unsafe_allow_html=True)


def toggle_dark_mode():
    """
    在 sidebar 放置暗黑模式开关，并在页面注入 dark.css（如果开启）。
    支持暗黑模式的文件读取也做类似的健壮性处理。
    """
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    # Sidebar 开关
    st.sidebar.checkbox("🌙 暗黑模式", key="dark_mode")

    # 根据状态注入暗黑补丁
    if st.session_state.dark_mode:
        dark_css_text = ""
        try:
            dark_css_text = dark_css_path.read_text(encoding="utf-8")
            logger.info(f"Successfully loaded dark mode CSS from: {dark_css_path}")
        except FileNotFoundError:
            logger.warning(f"dark.css not found at {dark_css_path}. Dark mode may not be fully functional.")
            # 这里可以添加一个非常基础的暗黑样式作为绝对最低限度的回退，或者留空
        except Exception as e:
            logger.error(f"Error reading dark.css: {e}")

        if dark_css_text:
            st.markdown(f"<style>{dark_css_text}</style>", unsafe_allow_html=True)
