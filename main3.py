import streamlit as st
import pandas as pd

st.title("Biểu đồ phổ điểm thi lớp 10")

df = pd.read_csv("diemthi10.csv")

st.write("Dữ liệu:")
st.dataframe(df)

st.write("Biểu đồ môn Toán")
st.bar_chart(df, x="diem", y="Mon Toan (So HS)")

st.write("Biểu đồ môn Văn")
st.bar_chart(df, x="diem", y="Mon Ngu Van (So HS)")

st.write("Biểu đồ môn Anh")
st.bar_chart(df, x="diem", y="Mon Tieng Anh (So HS)")