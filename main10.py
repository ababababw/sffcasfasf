import streamlit as st

st.image(r"c:\Users\Admin\Downloads\Gemini_Generated_Image_gasiu5gasiu5gasi.png")

appetizer = {
    'Khoai tây chiên (20k)': 20,
    'Salad gà (25k)': 25,
    'Bắp rang bơ (15k)': 15,
    'Gà viên chiên (30k)': 30
}

main = {
    'Gà rán truyền thống (45k)': 45,
    'Gà cay Hàn Quốc (55k)': 55,
    'Gà sốt mật ong (50k)': 50,
    'Burger gà (40k)': 40,
    'Combo gà + khoai + nước (70k)': 70
}

dessert = {
    'Kem vani (15k)': 15,
    'Trà sữa (25k)': 25,
    'Nước ngọt (10k)': 10,
    'Sữa chua (12k)': 12
}

with st.form("Thực đơn gà rán NLM"):
    options1 = st.multiselect("🍟 Món khai vị bạn chọn?", list(appetizer.keys()))
    options2 = st.multiselect("🍗 Món chính bạn chọn?", list(main.keys()))
    options3 = st.multiselect("🍨 Món tráng miệng bạn chọn?", list(dessert.keys()))

    submitted = st.form_submit_button("Submit")

    if submitted:
        # Lưu lựa chọn vào session_state
        st.session_state["options1"] = options1
        st.session_state["options2"] = options2
        st.session_state["options3"] = options3
        st.session_state["show_bill"] = True

# Hiển thị hóa đơn nếu đã submit
if st.session_state.get("show_bill", False):
    st.write("## 🧾 Hóa đơn của bạn tại NLM")
    total = 0

    st.write("### 1. Món khai vị")
    if len(st.session_state["options1"]) == 0:
        st.write("Bạn chưa chọn món khai vị")
    else:
        for item in st.session_state["options1"]:
            qty = st.number_input(f"Số lượng {item}", min_value=1, value=1, step=1, key=f"qty_{item}")
            st.write(f"- {item} x {qty} : {appetizer[item] * qty}k")
            total += appetizer[item] * qty

    st.write("### 2. Món chính")
    if len(st.session_state["options2"]) == 0:
        st.write("Bạn chưa chọn món chính")
    else:
        for item in st.session_state["options2"]:
            qty = st.number_input(f"Số lượng {item}", min_value=1, value=1, step=1, key=f"qty_{item}")
            st.write(f"- {item} x {qty} : {main[item] * qty}k")
            total += main[item] * qty

    st.write("### 3. Món tráng miệng")
    if len(st.session_state["options3"]) == 0:
        st.write("Bạn chưa chọn món tráng miệng")
    else:
        for item in st.session_state["options3"]:
            qty = st.number_input(f"Số lượng {item}", min_value=1, value=1, step=1, key=f"qty_{item}")
            st.write(f"- {item} x {qty} : {dessert[item] * qty}k")
            total += dessert[item] * qty

    st.success(f"💰 Tổng tiền của bạn là: {total}k")
