import asyncio
from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse

router = APIRouter()


async def generate_stream():
    chunks = [
        "Analyzing query...",
        "Retrieving graph entities...",
        "Performing multi-hop traversal...",
        "Synthesizing answer...",
        "Finalizing response..."
    ]

    for chunk in chunks:
        yield {
            "event": "message",
            "data": chunk
        }

        await asyncio.sleep(1)


@router.get("/stream")
async def stream():
    return EventSourceResponse(generate_stream())
    
# Add to main.py
from streaming import router as streaming_router

app.include_router(streaming_router)