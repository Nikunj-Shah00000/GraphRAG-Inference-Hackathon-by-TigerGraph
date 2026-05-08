import os
import chromadb
from openai import OpenAI
from app.utils.embeddings import get_embedding
from app.utils.metrics import Timer, calculate_cost

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chroma_client = chromadb.Client()
collection = chroma_client.create_collection("rag_docs")


def load_documents(documents):
    for i, doc in enumerate(documents):
        collection.add(
            documents=[doc],
            embeddings=[get_embedding(doc)],
            ids=[str(i)]
        )


def run_basic_rag(query):
    timer = Timer()
    timer.start()

    results = collection.query(
        query_embeddings=[get_embedding(query)],
        n_results=3
    )

    context = "\n".join(results["documents"][0])

    prompt = f"""
    Use the following context to answer the question.

    Context:
    {context}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    timer.stop()

    answer = response.choices[0].message.content

    usage = response.usage
    total_tokens = usage.total_tokens

    return {
        "pipeline": "Basic RAG",
        "answer": answer,
        "tokens": total_tokens,
        "latency": timer.elapsed(),
        "cost": calculate_cost(total_tokens)
    }