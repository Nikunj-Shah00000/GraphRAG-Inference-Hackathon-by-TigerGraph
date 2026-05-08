import os
import evaluate
from huggingface_hub import InferenceClient

client = InferenceClient(
    model="meta-llama/Llama-3.1-8B-Instruct",
    token=os.getenv("HF_TOKEN")
)

bertscore = evaluate.load("bertscore")

JUDGE_PROMPT = """
Question: {q}
Correct Answer: {correct}
System Answer: {answer}

Reply only PASS or FAIL.
"""



def evaluate_pipeline(outputs, references, questions):
    judge_results = []

    for answer, ref, q in zip(outputs, references, questions):
        prompt = JUDGE_PROMPT.format(
            q=q,
            correct=ref,
            answer=answer
        )

        verdict = client.chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=10,
            temperature=0
        )

        result = verdict.choices[0].message.content

        judge_results.append("PASS" in result.upper())

    bert = bertscore.compute(
        predictions=outputs,
        references=references,
        lang="en",
        rescale_with_baseline=True
    )

    return {
        "pass_rate": sum(judge_results) / len(judge_results),
        "bertscore": sum(bert["f1"]) / len(bert["f1"])
    }