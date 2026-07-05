import streamlit as st
import pandas as pd
import random

students = ["An", "Bình", "Cường", "Dung"]
subjects = ["Toán", "Lý", "Hóa", "Sinh", "Văn", "Sử", "Địa", "Anh", "Tin", "GDCD"]


def tao_bang():
    data = []

    for student in students:
        row = {"Tên": student}
        for subject in subjects:
            row[subject] = random.randint(0, 10)
        data.append(row)

    return pd.DataFrame(data)

st.title("Bảng điểm học sinh")

if "df" not in st.session_state:
    st.session_state.df = tao_bang()


if st.button("Random"):
    st.session_state.df = tao_bang()

st.dataframe(st.session_state.df, width="stretch")