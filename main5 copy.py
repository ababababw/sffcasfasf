import streamlit as st
import pandas as pd


data = pd.read_csv("D:\\pro 5\\data1.csv")

st.dataframe(data)

data_copy = data.copy()

data["toan"] = data["toan"].add([4, 0, 0, 0])
data["van"]  = data["van"].add([2, 0, 0, 0])
data["anh"]  = data["anh"].add([6, 0, 0, 0])

st.dataframe(data)