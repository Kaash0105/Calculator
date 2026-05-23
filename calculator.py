import streamlit as st

st.set_page_config(
    page_title="Math Calculator 🧮",
    layout="wide",
)

st.title(" ➕➖ Simple Maths Calculator ✖️➗")

number1 = st.number_input("Enter Number: ", value=0.0, key="num1")
operations = st.selectbox("Choose Operation", ["+", "-", "*", "/"])
number2 = st.number_input("Enter Number: ", value=0.0, key="num2")

result = 0
if st.button("Calculate"):
    if operations == "+":
        result = number1 + number2
    elif operations == "-":
        result = number1 - number2
    elif operations == "*":
        result = number1 * number2
    elif operations == "/":
        result = number1 / number2
    else:
        st.error("Invalid Operation")

    st.success(f"Result: {result}")

with st.bottom:
    st.caption("© MATHS CALCULATOR")

st.title("Percentage Calculator (%)")

number1 = st.number_input("Enter Number: ", value=0.0, key="per_num1")
operations = st.selectbox("Choose Operation", ["%"])
percentage = st.number_input("Enter Number: ", value=0.0, key="percentage")

result = 0
if st.button("Calculate Percentage", key="calc_btn_2"):
    if operations == "%":
        result = number1 / percentage * 100
    else:
        st.error("Invalid Operation")
    st.success(f"Result: {result}")
