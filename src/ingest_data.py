from data_converter import convert
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd

def ingest(status):
    load_dotenv()

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    ASTRA_API_KEY = os.getenv("ASTRA_API")
    DB_ENDPOINT = os.getenv("DB_ENDPOINT")
    DB_ID = os.getenv("DB_ID")

    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")

    vector_store = AstraDBVectorStore(collection_name = "Ayurvedic_Bot",
                                    embedding = embeddings,
                                    api_endpoint = DB_ENDPOINT,
                                    token = ASTRA_API_KEY,
                                    namespace = "symptoms")

    if status == None:
        symp_docs = convert()
        inserted_ids = vector_store.add_documents(symp_docs)
    else:
        return vector_store
    
    return vector_store

# if __name__ == "__main__":
#     vector_store = ingest("done")
#     results = vector_store.similarity_search("I have chest pain")
#     symptom_names = []

#     for res in results:
#         symptom_name = res.metadata.get("Symptom", "Unknown")
#         # print(f"* {res.page_content} [{res.metadata}]")
#         symptom_names.append(symptom_name)

#     print(symptom_names[0])




