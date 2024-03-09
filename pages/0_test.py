import streamlit as st


output = st.selectbox("Wybierz wartość", options=["a", "b", "c"], index=0)
st.markdown(output)


slider_output = st.slider(
    "Wybierz wartosć", min_value=0., step=0.001, max_value=10., value=[3., 5.],
    key="slider 1")

st.markdown(slider_output)

st.color_picker("Wybierz kolor")

logical = st.toggle("Toggle value", value=True)
st.markdown(logical)

st.number_input("Wybierz liczbę:", min_value=1., max_value=4., step=0.1,
                value=2.5)