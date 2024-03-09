import streamlit as st
from streamlit_extras.grid import grid


left, right = st.columns(2)

with left:
    left.markdown("Left column")  # left.<...> and st.<...> are both correct
    left.markdown("Left column 123")  # left.<...> and st.<...> are both correct

with right:
    selected = right.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
    right.markdown(selected)


st.divider()

a, _, b = st.columns([2, 4, 3])

with a:
    value = a.toggle("Toggle")
    st.markdown(value)

with b:
    values = b.multiselect("Multiselect", [1, 2, 3])
    st.markdown(values)


st.divider()

my_grid = grid(2, [1, 2, 3], 1)

for i in range(20):
    cont = my_grid.container()
    with cont:
        cont.markdown(i)
        cont.markdown(i*2)
