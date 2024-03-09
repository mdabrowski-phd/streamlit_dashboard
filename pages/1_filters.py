import streamlit as st
import pandas as pd
from streamlit_extras.grid import grid


st.set_page_config(page_title="Filters", page_icon="", layout="wide")

st.markdown("""
    <style>
        div[data-testid="stMarkdownContainer"] > p {
        font-size: 1.2rem;
        }
    </style>
    """, unsafe_allow_html=True)

df = st.session_state["df"]
orig_df = st.session_state["orig_df"]

filter_column, _, boolean = st.columns([5, 1, 5])

with filter_column:
    filter_column.subheader("Filter columns")

    selected_columns = filter_column.multiselect(
        "Choose columns", options=["ALL"] + list(orig_df.columns), default=list(orig_df.columns))

    if "ALL" in selected_columns:
        selected_columns = list(orig_df.columns)

    df = orig_df[selected_columns]
    st.session_state.df = df

with boolean:
    boolean.subheader("Filter boolean values")

    boolean_df = st.session_state.df[selected_columns].select_dtypes("bool")

    for column in boolean_df.columns:
        df = st.session_state.df
        unique_values = df[column].unique()

        with boolean.expander(f"Filter `{column}` column"):
            selected_categories = st.multiselect(
                f"Select categories for {column}", options=unique_values,
                default=unique_values)

            use_nans = st.toggle("Use NaN values", key=f"{column} toggle", value=True)

            df = df[
                df[column].isin(selected_categories) | (df[column].isna() if use_nans else False)]
            st.session_state.df = df

st.divider()

numeric, _, categoric = st.columns([5, 1, 5])

with numeric:
    # Filter numeric columns
    st.subheader("Filter numeric value")
    numeric_df = df.select_dtypes("number")
    numeric_grid = grid(2)

    for column in numeric_df.columns:
        with numeric_grid.expander(f"Filter `{column}` column"):
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

with categoric:
    st.subheader("Filter categoric values")

    categoric_df = st.session_state.df[selected_columns].select_dtypes("object")
    categoric_df = categoric_df.loc[:, categoric_df.nunique() < 8]

    categoric_grid = grid(2)

    for column in categoric_df.columns:
        df = st.session_state.df
        unique_values = df[column].unique()
        unique_values = unique_values[~pd.isna(unique_values)]

        with categoric_grid.expander(f"Filter `{column}` column"):
            selected_categories = st.multiselect(
                f"Select categories for {column}", options=unique_values,
                default=unique_values)

            use_nans = st.toggle("Use NaN values", key=f"{column} toggle", value=True)

            df = df[df[column].isin(selected_categories) | (df[column].isna() if use_nans else False)]
            st.session_state.df = df



st.divider()
st.markdown(f"Dataframe shape: {df.shape}")
st.dataframe(df)
