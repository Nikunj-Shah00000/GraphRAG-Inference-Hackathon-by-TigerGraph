import os
import networkx as nx
from openai import OpenAI
from app.utils.metrics import Timer, calculate_cost

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

graph = nx.Graph()


def build_graph():
    graph.add_edge("Transformer", "Attention")
    graph.add_edge("Attention", "Efficiency")
    graph.add_edge("Efficiency", "Inference")
    graph.add_edge("Inference", "Token Reduction")


build_graph()



def retrieve_graph_context(query):
    matched_nodes = []

    for node in graph.nodes:
        if node.lower() in query.lower():
            matched_nodes.append(node)

    related = set()

    for node in matched_nodes:
        neighbors = graph.neighbors(node)
        related.update(neighbors)

    context = " ".join(list(related))

    return context



def run_graphrag(query):
    timer = Timer()
    timer.start()

    graph_context = retrieve_graph_context(query)

    prompt = f"""
    Use the graph context below.

    Graph Context:
    {graph_context}

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
        "pipeline": "GraphRAG",
        "answer": answer,
        "tokens": total_tokens,
        "latency": timer.elapsed(),
    }