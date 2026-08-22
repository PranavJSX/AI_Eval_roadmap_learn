from decorators import *
import random


@retry_on_failure(retires=2, delay=1)
def mock_flaky_llm_call(prompt):
    import random

    if random.random() < 0.7:
        raise ConnectionError("API Rate Limit Reached")
    return f"Response to : {prompt}"


@log_eval_run
@retry_on_failure(retires=3, delay=0.5)
def mock_api_eval(prompt, model="gpt-4o"):
    # Simulate a flaky API that fails 50% of the time
    if random.random() < 0.5:
        raise ConnectionError("API connection dropped!")
    return f"Evaluated prompt '{prompt}' successfully."


def main():

    # mock_flaky_llm_call("dance with me")
    result = mock_api_eval("Is Earth flat?", model="gpt-4o")


if __name__ == "__main__":
    main()
