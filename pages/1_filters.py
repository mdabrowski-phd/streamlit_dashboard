import streamlit as st


st.set_page_config(page_title="Filters",
                   page_icon="")


if not hasattr(st.session_state, "data"):
    st.warning("No data uploaded")
else:
    st.dataframe(st.session_state.data)

print(type(st.session_state))
