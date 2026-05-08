from fastapi import FastAPI
from pydantic import BaseModel

from app.pipelines.llm_only import run_llm_only
from app.pipelines.basic_rag import run_basic_rag
from app.pipelines.graphrag import run_graphrag

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {
        "message": "GraphReduce AI API Running"
    }


@app.post("/benchmark")
def benchmark(request: QueryRequest):
    query = request.query

    llm_result = run_llm_only(query)
    rag_result = run_basic_rag(query)
    graph_result = run_graphrag(query)

    return {
        "query": query,
        "results": [
            llm_result,
            rag_result,
            graph_result
        ]
    }