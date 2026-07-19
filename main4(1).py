import streamlit as st

st.title("Tính tiền tiết kiệm")

tien = st.number_input("Tiền gửi ban đầu", 0)
lai = st.number_input("Lãi suất mỗi tháng (%)", min_value=0.0, max_value=2.0)
so_thang = st.number_input("kỳ hạn (tháng)", 1)
gui_them = st.number_input("Gửi thêm mỗi tháng", 0)

if st.button("Tính"):
    lai = lai / 100
    tien_cuoi = tien

    for i in range(int(so_thang)):
        tien_cuoi = tien_cuoi + tien_cuoi * lai + gui_them

    st.write("Số tiền nhận được:", int(tien_cuoi), "VNĐ")