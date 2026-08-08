import pandas as pd
import streamlit as st

df = pd.read_csv("data5.8.csv")

so_gio_hoc = df["Số Giờ Học"]

itnhat = so_gio_hoc[0]
for i in so_gio_hoc:
    if i < itnhat:
        itnhat = i

nhieunhat = so_gio_hoc[0]
for i in so_gio_hoc:
    if i > nhieunhat:
        nhieunhat = i

tb = sum(so_gio_hoc) / len(so_gio_hoc)
trungvi = so_gio_hoc.median()
xuathiennhieunhat = so_gio_hoc.mode()

st.write("giá trị nhỏ nhất:", itnhat)
st.write("giá trị nhiều nhất:", nhieunhat)
st.write("trung binhg:", tb)
st.write("trung vị:", trungvi)
st.write("xuất hiện nhiều nhất:", xuathiennhieunhat)

gioi = df[df["Điểm Số"] >= 80]

diachi = gioi["Địa Chỉ"]

st.write("\nThành phố có nhiều điểm giỏi nhất:")
st.write(diachi.mode())