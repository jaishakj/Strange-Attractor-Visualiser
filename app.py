import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Strange Attractor Visualiser",
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide all streamlit chrome
st.markdown("""
<style>
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    [data-testid="stAppViewContainer"] { padding: 0; }
    [data-testid="stHeader"] { display: none; }
</style>
""", unsafe_allow_html=True)

html_content = Path(__file__).parent / "index.html"
components.html(
    html_content.read_text(),
    height=800,
    scrolling=False
)
