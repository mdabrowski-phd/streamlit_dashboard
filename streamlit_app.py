import streamlit as st
import pandas as pd
from st_pages import Page, show_pages


st.set_page_config(page_title="My first dashboard",
                   page_icon="📈")


show_pages(
    [
        Page("streamlit_app.py", "Custom name (main)", "💻", is_section=False),
        Page("pages/filters.py", "Filters", "🔍"),
        Page("pages/charts.py", "Charts", "📊"),
        Page("pages/test.py", "Test page", "📝"),
    ]
)

st.markdown(st.secrets["test_secret"])

st.title("My first dashboard")
st.markdown("#### This **dashboard** supports *markdown*")
st.text("Plain text")
st.markdown("Plain text")
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.header("Nagłówek")

st.divider()

st.info("Informacja")
st.error("error")
st.warning("Ostrzeżenie")
st.success("Sukces")

st.divider()

st.sidebar.title("Sidebar")
st.sidebar.markdown("Tekst w markdown")
st.sidebar.info("Informacja")

st.sidebar.divider()

csv_file = st.sidebar.file_uploader("Upload your file", type=[".csv"])

if csv_file:  # is not None:
    try:
        df = pd.read_csv(csv_file)
        st.session_state["df"] = df
        st.session_state["orig_df"] = df.copy()
    except Exception as e:
        st.sidebar.error(e)