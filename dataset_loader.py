# Real Dataset Loader
from datasets import load_dataset


def load_research_dataset():
    dataset = load_dataset(
        "scientific_papers",
        "pubmed",
        split="train[:100]"
    )

    return dataset


def load_legal_dataset():
    dataset = load_dataset(
        "lex_glue",
        "eurlex",
        split="train[:100]"
    )

    return dataset


def load_healthcare_dataset():
    dataset = load_dataset(
        "medical_questions_pairs",
        split="train[:100]"
    )

    return dataset