from adaptive_retrieval import adaptive_retrieval


@app.post("/adaptive")
def adaptive_query(request: QueryRequest):

    result = adaptive_retrieval(request.query)

    return {
        "query": request.query,
        "result": result
    }