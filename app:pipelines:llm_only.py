import os
from openai import OpenAI
from app.utils.metrics import Timer, calculate_cost

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run_llm_only(query):
    timer = Timer()
    timer.start()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )

    timer.stop()

    answer = response.choices[0].message.content

    usage = response.usage
    total_tokens = usage.total_tokens

    return {
        "pipeline": "LLM Only",
        "answer": answer,
        "tokens": total_tokens,
        "latency": timer.elapsed(),
        "cost": calculate_cost(total_tokens)
    }