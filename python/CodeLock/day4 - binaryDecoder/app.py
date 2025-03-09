import streamlit as st
from string import ascii_letters as char

st.set_page_config(page_title="BinaryDecoder", page_icon="💤", layout="centered")

st.title("BinaryDecoder")
st.write("This app converts binary numbers to letters and so on.")
output = []
binary_numbers = st.text_input("Enter binary numbers:")
if binary_numbers:
    binary_numbers = binary_numbers.split()
    for binary_number in binary_numbers:
        try:
            output.append(chr(int(binary_number, 2)))
        except:
            st.write("Invalid binary number.")
            
output = "".join(output)
st.write(output)
