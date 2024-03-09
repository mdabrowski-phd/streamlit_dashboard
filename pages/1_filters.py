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

# Filter numeric columns
st.subheader("Filter numeric value")
numeric_df = df.select_dtypes("number")

for column in numeric_df.columns:
    with st.expander(f"Filter {column} column"):
        n_unique = df[column].nunique()
        column_min = df[column].min()
        column_max = df[column].max()
        unique_values = df[column].unique()
        if n_unique > 4:
            selected_min, selected_max = st.slider(
                f"Select range for {column}", min_value=column_min,
                max_value=column_max, value=[column_min, column_max])
        else:
            selected_min = st.selectbox(f"Select min.", options=sorted(unique_values),
                                        index=0)
            selected_max = st.selectbox(f"Select max.", options=sorted(unique_values),
                                        index=n_unique - 1)

        use_nans = st.toggle("Use NaN values", value=True, key=f"{column} toggle")

        df = df[((df[column] <= selected_max)
                & (df[column] >= selected_min))
                | (df[column].isna() if use_nans else False)]

        st.session_state.df = df
st.divider()
st.dataframe(df)


# if not hasattr(st.session_state, "data"):
#     st.warning("No data uploaded")
# else:
#     st.dataframe(st.session_state.data)


