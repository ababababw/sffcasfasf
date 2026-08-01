import streamlit as st
import pandas as pd


df = pd.read_csv(r"D:\pro 5\data\data5.6_2.csv")

st.subheader("dữ liệu gốc")
st.write("Số dòng:", len(df))
st.dataframe(df)

dfxoatrung = df.drop_duplicates().reset_index(drop=True)
st.subheader("sau khi xóa trùng lặp")
st.write("Số dòng:", len(dfxoatrung))
st.dataframe(dfxoatrung)

dfxoanone = df.dropna().reset_index(drop=True)
st.subheader("sau khi xóa None")
st.write("Số dòng:", len(dfxoanone))
st.dataframe(dfxoanone)

