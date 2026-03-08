from langchain_neo4j import Neo4jGraph
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()


graph = Neo4jGraph(
    url="neo4j://127.0.0.1:7687",
    username="neo4j",
    password="1234567890",
    refresh_schema=True
)

llm = ChatGroq(
    # model="llama-3.3-70b-versatile",
    model = "llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

def extract_entities(query):
    prompt = f"""
        Extract important entities from the query.

        Return a Python list of keywords.

        Query:
        {query}

        Example:
        Input: "IAM roles failing when calling Lambda"
        Output: ["IAM","roles","Lambda"]
    """
    result = llm.invoke(prompt).content
    try:
        entities = eval(result)
        return entities
    except:
        return query.split()
    
def graph_retrieve_entities(entities):
    cypher = """
        MATCH (n)-[r]-(m)
        WHERE any(e IN $entities WHERE toLower(n.id) CONTAINS toLower(e)
        OR toLower(m.id) CONTAINS toLower(e))
        RETURN n.id AS source, type(r) AS relationship, m.id AS target
        LIMIT 25
    """
    results = graph.query(cypher, {"entities": entities})
    context = "\n".join(
        f"{r['source']} --{r['relationship']}--> {r['target']}"
        for r in results
    )
    return context

def graph_rag_retrieve(query):
    entities = extract_entities(query)
    print("Entities:", entities)
    graph_context = graph_retrieve_entities(entities)
    return graph_context

if __name__ == "__main__":
    print(graph_rag_retrieve("Why is my IAM roles access failing when calling a lambda?"))