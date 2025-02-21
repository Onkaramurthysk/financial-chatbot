import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.chatbot import load_data, get_financial_answer

st.title("💬 Financial Q&A Chatbot")
st.write("Upload a financial dataset and ask questions about the data.")

# Upload Excel file
uploaded_file = st.file_uploader("Upload your financial Excel file", type=["xlsx"])
if uploaded_file:
    data = load_data(uploaded_file)
    st.write("Preview of uploaded data:", data.head())

    # User input
    user_query = st.text_input("Ask a financial question:")

    if st.button("Get Answer"):
        if user_query:
            answer = get_financial_answer(user_query, data)
            st.success(answer)
        else:
            st.warning("Please enter a question.")
