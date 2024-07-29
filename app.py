import streamlit as st
import os
from langchain_astradb import AstraDBVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import sys
sys.path.append(os.path.abspath("src"))

from src.generation import generate

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
ASTRA_API_KEY = os.getenv("ASTRA_API")
DB_ENDPOINT = os.getenv("DB_ENDPOINT")
DB_ID = os.getenv("DB_ID")

# Set up the vector store
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vector_store = AstraDBVectorStore(collection_name="Ayurvedic_Bot",
                                   embedding=embeddings,
                                   api_endpoint=DB_ENDPOINT,
                                   token=ASTRA_API_KEY,
                                   namespace="symptoms")

if 'history' not in st.session_state:
    st.session_state.history = []

def generate_response(query):
    result = generate(vector_store, query)
    st.session_state.history.append(f"User: {query}")
    st.session_state.history.append(f"Bot: {result}")
    return result

st.title("Ayurvedic Remedy Bot")
st.write("Enter your symptom to find relevant Ayurvedic remedies.")

for message in st.session_state.history:
    st.write(message)


query = st.text_input("Enter your Problem:")
if st.button("Submit"):
    if query:
        response = generate_response(query)
        st.write(f"**Bot:** {response}")



