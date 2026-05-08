from pipelines.basic_rag import run_basic_rag
from pipelines.graphrag import run_graphrag


def detect_query_complexity(query: str):
    """
    Determine retrieval strategy based on query complexity.
    """

    multi_hop_keywords = [
        "relationship",
        "impact",
        "connected",
        "compare",
        "between",
        "history",
        "reason",
        "why",
        "cause",
        "effect",
        "linked",
    ]

    score = 0

    for word in multi_hop_keywords:
        if word.lower() in query.lower():
            score += 1

    if score >= 3:
        return "graph"

    elif score >= 1:
        return "hybrid"

    return "vector"


def adaptive_retrieval(query: str):
    strategy = detect_query_complexity(query)

    if strategy == "graph":
        result = run_graphrag(query)

    elif strategy == "hybrid":
        graph_result = run_graphrag(query)
        rag_result = run_basic_rag(query)

        combined_answer = f"""
        GRAPH RESULT:
        {graph_result['answer']}

        VECTOR RESULT:
        {rag_result['answer']}
        """

        result = {
            "pipeline": "Hybrid Retrieval",
            "answer": combined_answer,
            "tokens": graph_result["tokens"] + rag_result["tokens"],
            "latency": max(
                graph_result["latency"],
                rag_result["latency"]
            ),
            "cost": graph_result["cost"] + rag_result["cost"]
        }

    else:
        result = run_basic_rag(query)

    result["strategy"] = strategy

    return result