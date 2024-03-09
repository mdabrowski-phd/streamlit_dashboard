import streamlit as st
import pandas as pd
from streamlit_extras.grid import grid


st.set_page_config(page_title="Data analytics", page_icon="📈", layout="wide")
st.markdown("""
    <style>
        div[data-testid="stMarkdownContainer"] > p {
        font-size: 1.2rem;
        }
    </style>
    """, unsafe_allow_html=True)


if not hasattr(st.session_state, "df"):
    st.session_state["df"] = pd.DataFrame()

df = st.session_state["df"]
orig_df = st.session_state["orig_df"]


filter_cols, _, boolean = st.columns([5, 1, 5])

with filter_cols:
    # Filter columns
    st.subheader("Filter columns")
    selected_columns = st.multiselect(
        "Choose columns", options=(["ALL"] + list(orig_df.columns)), default=list(orig_df.columns))

    if "ALL" in selected_columns:  # there is no "select all", so this workaround
        selected_columns = list(orig_df.columns)

    df = orig_df[selected_columns]
    st.session_state.df = df

with boolean:
    # Filter boolean values
    st.subheader("Filter boolean values")
    boolean_df = st.session_state.df[selected_columns].select_dtypes(include="bool")
    boolean_grid = grid(2)

    for column in boolean_df.columns:
        df = st.session_state.df
        with boolean_grid.expander(f"Filter `{column}` column"):
            unique_values = df[column].unique()

            selected_values = st.multiselect(f"Select values for {column}.", options=sorted(unique_values), default=sorted(unique_values))

            use_nans = st.toggle("Use NaN values", key=f"toggle {column}", value=True)

            df = df[(df[column].isin(selected_values)) | (
                df[column].isna() if use_nans else False)]
            st.session_state.df = df

st.divider()


numeric, _, categoric = st.columns([5, 1, 5])

with numeric:
    # Filter numeric values
    st.subheader("Filter numeric values")
    numeric_df = st.session_state.df[selected_columns].select_dtypes(include="number")
    numeric_grid = grid(2)

    for column in numeric_df.columns:
        df = st.session_state.df
        with numeric_grid.expander(f"Filter `{column}` column"):
            column_min = df[column].min()
            column_max = df[column].max()
            n_unique = df[column].nunique()
            unique_values = df[column].unique()

            if n_unique > 4:
                selected_min, selected_max = st.slider(
                    f"Select range for {column}", min_value=column_min, max_value=column_max,
                    value=[column_min, column_max])
            else:
                selected_min = st.selectbox("Select min.", options=sorted(unique_values), index=0, key=f"select_min {column}")
                selected_max = st.selectbox("Select max.", options=sorted(unique_values), index=len(unique_values)-1, key=f"select_max {column}")

            use_nans = st.toggle("Use NaN values", key=f"toggle {column}", value=True)

            df = df[(df[column] <= selected_max) & (df[column] >= selected_min) | (df[column].isna() if use_nans else False)]
            st.session_state.df = df


with categoric:
    # Filter categoric values
    st.subheader("Filter categoric values")
    categoric_df = st.session_state.df[selected_columns].select_dtypes(include="object")
    categoric_df = categoric_df.loc[:, categoric_df.nunique() < 8]  # arbitrary value
    categoric_grid = grid(2)

    for column in categoric_df.columns:
        df = st.session_state.df
        with categoric_grid.expander(f"Filter `{column}` column"):
            unique_values = df[column].unique()
            unique_values = unique_values[~pd.isna(unique_values)]

            selected_categories = st.multiselect(f"Select categories for {column}", options=unique_values,
                                                 default=unique_values)
            use_nans = st.toggle("Use NaN values", key=f"toggle {column}", value=True)

            df = df[df[column].isin(selected_categories) | (df[column].isna() if use_nans else False)]

            st.session_state.df = df

st.divider()

df = st.session_state.df
st.markdown(f"Dataframe shape: {df.shape}")
st.dataframe(df)
