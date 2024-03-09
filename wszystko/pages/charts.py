import streamlit as st
import pandas as pd
import plotly.express as px
import io


st.set_page_config(layout="wide")
st.markdown("""
    <style>
        div[data-testid="stMarkdownContainer"] > p {
        font-size: 1.2rem;
        }
    </style>
    """, unsafe_allow_html=True)

if hasattr(st.session_state, "df"):
    df = st.session_state.df.iloc[:10000]
else:
    df = pd.DataFrame()

numeric_columns = list(df.select_dtypes("number").columns)
boolean_columns = list(df.select_dtypes(bool).columns)
categoric_columns = list(df.columns[df.nunique() < 8])

plot_type, _ = st.columns([1, 3])

with plot_type:
    chart_type = plot_type.selectbox("Choose plot type",
                                     ["Histogram", "Barplot", "Boxplot", "Scatterplot"])

fig = None

if chart_type == "Histogram":
    selectbox, _, _ = st.columns(3)
    with selectbox:
        column = selectbox.selectbox("Choose a column for the histogram", numeric_columns)

    fig = px.histogram(df, x=column)

elif chart_type == "Barplot":
    selectbox_categoric, selectbox_numeric, selectbox_metric = st.columns(3)

    with selectbox_categoric:
        category_col = selectbox_categoric.selectbox(
            "Choose a categoric column for the barplot", categoric_columns + boolean_columns)
    with selectbox_numeric:
        numeric_col = selectbox_numeric.selectbox(
            "Choose a numeric column for the barplot", numeric_columns + boolean_columns)
    with selectbox_metric:
        metric = selectbox_metric.selectbox("Choose an aggregation metric", ["mean", "median", "sum"])

    grouped_df = df.groupby(category_col)[numeric_col].agg(metric)
    fig = px.bar(df, x=grouped_df.index, y=grouped_df)

elif chart_type == "Boxplot":
    selectbox_categoric, selectbox_numeric, _ = st.columns(3)

    with selectbox_categoric:
        category_col = selectbox_categoric.selectbox(
            "Choose a categoric column for the boxplot", categoric_columns + boolean_columns)
    with selectbox_numeric:
        numeric_col = selectbox_numeric.selectbox(
            "Choose a numeric column for the boxplot", numeric_columns + boolean_columns)

    fig = px.box(df, x=category_col, y=numeric_col)

elif chart_type == "Scatterplot":
    selectbox_column_1, selectbox_column_2, _ = st.columns(3)

    with selectbox_column_1:
        column_1 = selectbox_column_1.selectbox(
            "Choose the first column for the scatter plot", numeric_columns)
    with selectbox_column_2:
        column_2 = selectbox_column_2.selectbox(
            "Choose the second column for the scatter plot", numeric_columns)

    fig = px.scatter(df, x=column_1, y=column_2)

fig.update_traces(marker=dict(line=dict(width=1, color="black")))
fig.update_xaxes(tickfont=dict(size=16))
fig.update_yaxes(tickfont=dict(size=16))
fig.update_layout(xaxis_title=dict(font=dict(size=20)), yaxis_title=dict(font=dict(size=20)),
                  width=600, height=600)  # only after downloading

if fig:
    st.plotly_chart(fig, use_container_width=True)

    def to_html(fig):
        buf = io.StringIO()
        fig.write_html(buf, include_plotlyjs="cdn")
        buf.seek(0)
        return buf.getvalue()

    html_data = to_html(fig)
    st.download_button(
        label="Pobierz wykres jako HTML",
        data=html_data,
        file_name="plot.html",
        mime="text/html"
    )
