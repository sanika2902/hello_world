import streamlit as st
from demo import area_circle

st.header("Hello,streamlit!")
st.write("This is a simple calculation application")        

radius=st.text_input("Enter radious:")

if st.button("Calculate Area"):

    area=area_circle(int(radius))
    st.write(f"The are of circle with radius {radius} is {area}.")