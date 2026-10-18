import pytest
import asyncio
import json
from main import evaluate_batch

@pytest.mark.asyncio
async def test_runner():

    with open("dataset.json", 'r') as file:
        dataset = json.load(file)

    tasks = [evaluate_batch(item, test_id=idx+1) for idx, item in enumerate(dataset)]
    results = await asyncio.gather(*tasks)

    assert len(results) == len(dataset), "Result numbers match the length of the dataset"

    for report in results:
        print(f"\n Report for testid = {report.test_id}")
        print(f"\n Status: {report.pass_fail} | Score: {report.score}")
        print(f"\n Feedback: {report.feedback}")

        assert report.pass_fail == "PASS"
        assert report.score > 0.9

