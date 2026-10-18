import pytest 
import asyncio

async def mock_llm_call(prompt:str):
    await asyncio.sleep(0.5)

    return {"answer":"Paris", "confidence":0.95}

@pytest.mark.smoke
@pytest.mark.asyncio
async def test_llm_output():
    response = await mock_llm_call("What is the capital of France ?")
    assert response["answer"] == "Paris"
    assert response["confidence"] > 0.8

