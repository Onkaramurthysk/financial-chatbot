import os
import pandas as pd
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# Load API keys from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Chat Model
llm = ChatGroq(model_name="llama-3.3-70b-versatile")

# Load financial data
def load_data(file_path="backend/financial_data.xlsx"):
    return pd.read_excel(file_path)  # Ensure file is an Excel sheet

# Process user query
def get_financial_answer(query, data):
    """
    Generates a financial answer based on both structured (Excel) data and the chatbot's knowledge.
    """
    prompt_template = PromptTemplate.from_template(
        "Based on the following financial dataset and your expertise, answer this question:\n\n"
        "Financial Data:\n{data}\n\n"
        "User Query:\n{query}\n\n"
        "Provide a clear and concise answer."
    )
    
    response = (prompt_template | llm).invoke({'data': data.to_string(), 'query': query})
    return response.content
