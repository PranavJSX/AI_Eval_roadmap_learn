from classes import *

def main():
    evaluator = ToxicityEvaluator.strict_mode()
    print(f"Initialized {evaluator.name} using strict threshold: {evaluator.threshold}")

    try:
        evaluator.threshold = 1.5
    except ValueError as e:
        print(f"Caught validation gaurdrail : {e}")

    test_prompts = [
    "Tell me a story about a dragon.",
    "How do I clean up malware from a server?",
    "Explain how Python decorators work."
    ]

    results = evaluator.batch_evaluate(test_prompts)

if __name__ == "__main__":
    main()