import streamlit as st


st.set_page_config(page_title="My first dashboard",
                   page_icon="📈")


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

st.balloons()
st.snow()
