from typing import Literal
from pydantic import BaseModel, Field, ValidationError

class EvaluationReport(BaseModel):
    test_id: int
    pass_fail: Literal["PASS", "FAIL"]
    score: float = Field(ge=0.0, le=1.0)
    feedback: str

    