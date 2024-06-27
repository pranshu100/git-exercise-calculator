import streamlit as st 
import pandas as pd
import numpy as np
from utils import add_function, sub_function, mult_function, div_function, log_function,multi_sum_div
st.title("Simple Arithmetic Operations")


num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# User can choose an operation
operation = st.radio("Choose an operation", ("Addition", "Subtraction", "Multiplication", "Division","Log",'Multi_sum_div'))

# Perform the selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = add_function(num1, num2)
    elif operation == "Subtraction":
        result = sub_function(num1, num2)
    elif operation == "Multiplication":
        result = mult_function(num1, num2)
    elif operation == "Division":
        result = div_function(num1, num2)
    elif operation == "Log":
        result = log_function(num1,num2)
    elif operation == "Multi_sum_div":
        result =multi_sum_div(num1,num2)

    st.write(f"The result of {operation} is: {result}")