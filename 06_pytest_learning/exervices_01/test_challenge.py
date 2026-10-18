from typing import Literal
from pydantic import BaseModel, Field, ValidationError

class LLMEvaluationResult(BaseModel):
    pass_fail:Literal["PASS", "FAIL"]
    reasoning: str = Field(min_length=10)
    score:float = Field(ge=0.0, le=1.0)

def main():
    try:
        raw_llm_response = LLMEvaluationResult(
            pass_fail= "PASS",
            reasoning= "The model correctly identified the capital city.",
            score= 0.98
        )
        print("SUCCESS", raw_llm_response)
    except ValidationError as e:
        print("ERROR", e)

if __name__=="__main__":
    main()  

    