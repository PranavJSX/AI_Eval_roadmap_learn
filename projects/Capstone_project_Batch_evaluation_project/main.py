from models import EvaluationReport
import asyncio

async def evaluate_batch(obj, test_id):
    response = {}
    await asyncio.sleep(0.8)
    if obj["expected_keyword"] in obj["app_response"]:
        pass_fail = "PASS"
        score = 0.95
        response = {"test_id":test_id, "pass_fail":pass_fail, "score":score, "feedback":"Correct response"}

    else:
        response = {"test_id":test_id, "pass_fail":"FAIL", "score":0.2, "feedback":"Incorrect response"}

    return EvaluationReport.model_validate(response)


    