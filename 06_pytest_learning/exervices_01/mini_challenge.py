from typing import Literal
import asyncio
import pytest
from pydantic import BaseModel, Field
# from test_challenge import LLMEvaluationResult

class LLMEvaluationResult(BaseModel):
    pass_fail:Literal["PASS", "FAIL"]
    score:float = Field(ge=0.0, le=1.0)

async def evaluate_response(query:str, response:str) -> LLMEvaluationResult:
    await asyncio.sleep(0.3)
    if query == "What is 2+2" and response == '4':
        return {"pass_fail": "PASS", "score": 0.9}

    return {"pass_fail":"FAIL", "score":0.0}

@pytest.mark.smoke
@pytest.mark.asyncio
async def test_llm_judge():
    response = await evaluate_response("What is 2+2", "4")
    # print(response)
    response_formated = LLMEvaluationResult.model_validate(response)
    assert response_formated.pass_fail == "PASS"
    assert response_formated.score > 0.7
    # print(":HERE",response_formated)



