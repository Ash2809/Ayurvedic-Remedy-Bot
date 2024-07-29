from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain
from data_converter import convert
from ingest_data import ingest
from dotenv import load_dotenv
import pandas as pd
import os

def generate(vector_store,query):
    medication_data = pd.read_csv(r"C:\Users\aashutosh kumar\projects\Ayurvedic-Remedy-Bot\data\Formulation-Indications.csv")
    class_labels = pd.read_csv(r"data\FormulationClass.csv")


    classes = dict(zip(class_labels["Class"],class_labels["Unnamed: 1"]))
    medication_data["Class"] = medication_data["Class"].map(classes)

    medication_data.dropna(inplace=True)

    load_dotenv()

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro",temperature = 0.8)

    # query = input("Enter your Problem: ")
    results = vector_store.similarity_search(query,k = 1)

    symptom_names = []

    for res in results:
        symptom_name = res.metadata.get("Symptom", "Unknown")
        print(f"* {res.page_content} [{res.metadata}]")
        symptom_names.append(symptom_name)

    print(symptom_names[0])
    search_term = symptom_names[0]

    result = medication_data[medication_data['Main Indications'].str.contains(search_term, case=False, na=False)]

    prompt = """You are a expert in ayurveda but only a retriver and with the given dataframe {dataframe},
    tell me the name of medicine , dispensing Pack size and Dose along with Precaution.
    Do not make up any answer and answer generously and show gratitude.Also present it in a good way
    and never mention the user that the dataframe was given.
    """

    df_string = result.to_string(index=False)

    prompt_template = PromptTemplate(template=prompt, input_variables=["dataframe"])
    output_parser = StrOutputParser()
    chain = LLMChain(llm=llm, prompt=prompt_template, output_parser=output_parser)

    result = chain.run(dataframe = df_string)

    return result

# if __name__ == "__main__":
#     vector_store = ingest("done")
#     query = "I have chest pain"
#     result = generate(vector_store,query)
#     print(result)
