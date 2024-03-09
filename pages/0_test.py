import streamlit as st
from streamlit_extras.grid import grid

st.markdown("""
        <style>
        p {font-size: 5.2rem;}
        
        li {font-size: 1.2rem !important;}
        
        div[data-testid="stMarkdownContainer"] > p{
            font-size: 1.5rem !important;
        }
        div[data-testid="stMarkdownContainer"] > ul > li{
            font-size: 5.3rem !important;
        }
        </style>""", unsafe_allow_html=True)


st.markdown("Test markdown paragraph")

st.markdown(""" Wypunktowana lista
- punkt 1
- punkt 2
""")


selected = st.selectbox("WYbierz", options=["a", "b", "c"])


# left, right = st.columns(2)
#
# with left:
#     left.markdown("Left column")  # left.<...> and st.<...> are both correct
#     left.markdown("Left column 123")  # left.<...> and st.<...> are both correct
#
# with right:
#     selected = right.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
#     right.markdown(selected)
#
#
# st.divider()
#
# a, _, b = st.columns([2, 4, 3])
#
# with a:
#     value = a.toggle("Toggle")
#     st.markdown(value)
#
# with b:
#     values = b.multiselect("Multiselect", [1, 2, 3])
#     st.markdown(values)
#
#
# st.divider()
#
# my_grid = grid(2, [1, 2, 3], 1)
#
# for i in range(20):
#     cont = my_grid.container()
#     with cont:
#         cont.markdown(i)
#         cont.markdown(i*2)
# #