from abc import ABC, abstractmethod
from typing import Dict, Any
from decorators import *


class BaseEvaluator(ABC):
    def __init__(self, name) -> str:
        self.name = name

    @property
    @abstractmethod
    def version(self) -> str:
        pass

    @abstractmethod
    def evalutate(self, prompt: str) -> Dict[str, Any]:
        pass

    def batch_evaluate(self, prompts: list[str]) -> Dict[str, Any]:
        print(f"n--- Batch running : {self.name} ({self.version}) ---")
        return [self.evalutate(p) for p in prompts]


class ToxicityEvaluator(BaseEvaluator):
    def __init__(self, threshold: float = 0.5):
        super().__init__(name="Toxicity Evaluator")
        self.threshold = threshold
        self._banned_words = ["toxic", "abuse", "malware", "exploit"]

    @property
    def version(self):
        return "v2.1.0"

    @property
    def threshold(self) -> float:
        return self._threshold

    @threshold.setter
    def threshold(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Threshold must be numeric")
        if not (0.0 <= value <= 1.0):
            raise ValueError("Threshold value not acceptable")

        self._threshold = value

    @classmethod
    def strict_mode(cls):
        return cls(threshold=0.1)

    @classmethod
    def relaxed_mode(cls):
        return cls(threshold=0.8)

    @time_and_log
    def evalutate(self, prompt: str) -> Dict[str, Any]:
        found_words = [word for word in self._banned_words if word in prompt.lower()]
        score = len(found_words) / len(self._banned_words)

        passed = score <= self.threshold
        return {
            "evaluator": self.name,
            "prompt": prompt,
            "threshold": self.threshold,
            "Passed": passed,
        }
