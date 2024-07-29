from langchain_core.documents import Document
from dotenv import load_dotenv
import pandas as pd

def convert():
    symptoms_data = pd.read_csv(r"C:\Users\aashutosh kumar\projects\Ayurvedic-Remedy-Bot\data\ayurvedic_symptoms_desc.csv")

    symptom_list = []
    for i,row in symptoms_data.iterrows():
        dict = {
            "Symptom" : row["Symptom"],
            "Description" : row["Description"] 
        }
        symptom_list.append(dict)

    symp_docs = []
    for dict in symptom_list:
        metadata = {"Symptom" : dict["Symptom"]}
        doc = Document(page_content = dict["Description"],metadata = metadata)
        symp_docs.append(doc)

    return symp_docs

# if __name__ == "__main__":
#     convert()    

