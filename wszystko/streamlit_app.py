import streamlit as st
import pandas as pd
from st_pages import Page, show_pages


st.set_page_config(page_title="My first dashboard", page_icon="📈")
st.title("Super streamlit dashboard")

show_pages(
    [
        Page("streamlit_app.py", "Project description", "💻", is_section=False),
        Page("pages/filters.py", "Filters", "🔍"),
        Page("pages/charts.py", "Charts", "📊"),
        Page("pages/sample_page.py", "Test page", "📝"),
    ]
)

st.markdown("This dashboard supports **markdown** and is *great* tool for `data analytics`")
st.text("It also supports preformatted text")
st.markdown(st.secrets["test_secret"])

st.header("Dashboard description")
st.divider()
st.markdown("In this dashboard we're going to create a great analytical tool")

st.divider()

st.info("Here is a piece of information")
st.warning("Here is a warning")
st.error("Here is an error message")
st.success("Success!")

st.divider()

# st.balloons()
# st.snow()

st.sidebar.title("Navigation")
st.sidebar.markdown("A piece of markdown code on the sidebar")

st.sidebar.divider()
csv_file = st.sidebar.file_uploader("Upload your data", type=[".csv"])
if csv_file:
    try:
        st.session_state.df = pd.read_csv(csv_file)
        st.session_state.orig_df = st.session_state.df.copy()
        st.sidebar.success("Dataframe created successfully")
    except Exception as e:
        st.sidebar.error(e)
