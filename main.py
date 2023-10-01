import streamlit as st
import pandas as pd


data = {
    'Series_1': [1,2,3,4,7],
    'Series_2': [10,20,30,100,250],
}

df = pd.DataFrame(data)


st.title("Our Streamlit App")
st.subheader("Introducing Streamlit In Automate Everything")
st.write(
    """
    First web app
    Enjoy It!!
    """)

st.write(df)
st.line_chart(df)
st.area_chart(df)

my_slider = st.slider('Celsius')
st.write(my_slider, 'in Fahrenheit is', my_slider * 9 / 5 + 32)