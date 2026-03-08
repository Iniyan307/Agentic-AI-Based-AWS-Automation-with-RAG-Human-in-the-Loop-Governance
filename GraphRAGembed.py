from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from typing import List
from langchain_experimental.graph_transformers.llm import GraphDocument
from utils.neo4j_add import add_graph
from utils.chunker import chunker
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import time

load_dotenv()

llm = ChatGroq(
    # model="llama-3.3-70b-versatile",
    model = "llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

llm_transformer = LLMGraphTransformer(
    llm=llm,
    allowed_nodes=["Service","User","Role","Policy","Credential","Account"],
    allowed_relationships=["USES","AUTHORIZES","ASSUMES","BELONGS_TO","ACCESS_TO"],
    node_properties=["description"],
    relationship_properties=["description"]
)

def process_pdf(file_path):
    print(f"processing: {file_path}")
    chunks = chunker(file_path)

    for i in range(0,len(chunks),3):
        batch = chunks[i:i+3]
        try:
            graph_documents = llm_transformer.convert_to_graph_documents(batch)
            add_graph(graph_documents)
            print(f"Processed batch {i} - {i+len(batch)}")

        except Exception as e:
            print(f"Batch {i} failed: {e}")
        time.sleep(6)
    print("Success......")


if __name__ == "__main__":
    try:
        process_pdf("data/pdf/AWSiamUserGuide_modified.pdf")
    except Exception as e:
        print(f"Error : {e}")