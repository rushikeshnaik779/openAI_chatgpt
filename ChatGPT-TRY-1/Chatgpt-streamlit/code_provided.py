import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: division by zero"
    else:
        return x / y

st.title("Calculator")

num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

operation = st.selectbox("Select an operation", ("Addition", "Subtraction", "Multiplication", "Division"))

if st.button("Calculate"):
    if operation == "Addition":
        result = add(num1, num2)
        st.write(f"{num1} + {num2} = {result}")
    elif operation == "Subtraction":
        result = subtract(num1, num2)
        st.write(f"{num1} - {num2} = {result}")
    elif operation == "Multiplication":
        result = multiply(num1, num2)
        st.write(f"{num1} * {num2} = {result}")
    elif operation == "Division":
        result = divide(num1, num2)
        st.write(f"{num1} / {num2} = {result}")
