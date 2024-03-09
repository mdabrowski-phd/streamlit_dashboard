import streamlit as st
import pandas as pd


st.set_page_config(page_title="My first dashboard",
                   page_icon="📈")


st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 200px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

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