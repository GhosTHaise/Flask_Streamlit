import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(size=1000)
data = pd.DataFrame(data,columns=["DistNormal"])
st.write(data.mean())
st.write(data.head())
st.write(data.describe())
st.dataframe(data)


st.title("Graphique :")

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(data["DistNormal"],linewidth=0.5)
st.pyplot(fig)




