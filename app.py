from data import dt
import pandas as pd
import streamlit as st

df = pd.DataFrame(dt[1:], columns=dt[0])

st.set_page_config(
    page_title="SIH 2023 Problem-Statement",
    page_icon="🪴",
    layout="wide",
)
st.write("Developed by [Jitendra-Kumar](https://www.jitendra.me)")

st.title("SIH 2023 Problem-Statement")

st.write("This is a simple example of a Streamlit app that displays a table.")



st.write(df)

