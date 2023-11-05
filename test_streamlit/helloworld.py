import streamlit as st
import pandas as pd
st.write("hello world ! I am GhosT")

dt = pd.DataFrame({
    "nom"  : ["Fitiavana","Finoana","Sambatra"],
    "age" : [20,22,53]
})

st.dataframe(dt)