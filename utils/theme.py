import streamlit as st
from pathlib import Path

MACOS_CSS = Path(__file__).parents[2] / "assets" / "macos.css"
DARK_CSS   = Path(__file__).parents[2] / "assets" / "dark.css"

def load_css():
    """一次性注入 macOS 浅色主题 CSS"""
    st.markdown(f"<style>{MACOS_CSS.read_text()}</style>", unsafe_allow_html=True)

def toggle_dark_mode():
    """Sidebar 暗黑模式开关，实时注入 dark.css"""
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False
    st.sidebar.checkbox("🌙 暗黑模式", key="dark_mode")
    if st.session_state.dark_mode:
        st.markdown(f"<style>{DARK_CSS.read_text()}</style>", unsafe_allow_html=True)
