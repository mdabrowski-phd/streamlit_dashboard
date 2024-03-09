import streamlit as st


st.set_page_config(page_title="Filters",
                   page_icon="")


df = st.session_state["df"]
orig_df = st.session_state["orig_df"]

st.subheader("Filter columns")

selected_columns = st.multiselect(
    "Choose columns",
    options=["ALL"] + list(orig_df.columns),
    default=list(orig_df.columns))

if "ALL" in selected_columns:
    selected_columns = list(orig_df.columns)

df = orig_df[selected_columns]
st.session_state.df = df

st.divider()





# if not hasattr(st.session_state, "data"):
#     st.warning("No data uploaded")
# else:
#     st.dataframe(st.session_state.data)


