from classes import *


def main():
    evaluator = PromptLengthEvaluator(max_allowed_characters=30)

    print("--- RUN 1: First time evaluating prompt A ---")
    res1 = evaluator("Is Python object-oriented?")

    print("\n--- RUN 2: Evaluating same prompt A again ---")
    res2 = evaluator("Is Python object-oriented?")

    print("\n--- RUN 3: Evaluating prompt B (exceeds limit) ---")
    res3 = evaluator(
        "Can you please give me a comprehensive breakdown of LLM evaluation metrics?"
    )


if __name__ == "__main__":
    main()
