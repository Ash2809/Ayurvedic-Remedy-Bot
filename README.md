# Ayurvedic-Remedy-Bot
This Bot is designed on the API of GEMINI.
Astra DB is used for storing the contextual embeddings of the ayurvedic Book.


The project flows in the following way:
Book-->Embeddings-->AstraDB

![alt text](0_WYv0_CaBmCTt7FXc.png)

User:
prompt-->llm-->query-->AstraDB-->Ranked Results-->Reranking-->llm-->Output


Advance RAG techniques such as reranking is used in the following code.
Experiments are present in the experiments.ipynb file while src folder contains Three Files:
-->ingest.py : Used to store data in DB
-->data_converter.py : Used to convert data from PDF to vector Embeddings
-->generation.py: Used to generate responses From llm

# NOTE: TO RUN THIS YOU NEED TO DOWNLOAD ALL THE DEPENDENCIES IN "requirements.py" ALSO PYTHON VERSION SHOULD BE 3.10.

IF YOU LIKED IT PLEASE FOLLOW MY GITHUB AND CONNECT ON LINKDIN https://www.linkedin.com/in/aashutosh-kumar-41024925a/


WILL BE DROPING PROJECTS LIKE THESE....


