from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseEvaluator(ABC):
    def __init__(self, name:str):
        self.name = name

    #Mandatory abstract method
    @abstractmethod
    def evaluate(self, prompt:str) -> Dict[str, Any]:
        '''Sublasses must implement this method'''
        pass

    #Mandatory abstract property
    @property
    @abstractmethod
    def evaluator_version(self) -> str:
        '''Subclasses must define a version string'''
        pass

    #Optional method
    def batch_evaluator(self, prompts: list[str]) -> list[Dict[str, Any]]:
        '''A helper method shared by all evaluators automatically '''
        print(f"Running batch evaluation for '{self.name}")
        return [self.evaluate(p) for p in prompts]

#Now we implement subclass for this parent abstract class
class ToxicityEvaluator(BaseEvaluator):
    def __init__(self, threshold :float = 0.8):
        super().__init__(name = "Toxicity Evaluator")
        self.threshold = threshold

    #Implementing requirement 1
    @property
    def evaluator_version(self) -> str:
        return "v1.2.0"

    #Implementing requirement 2
    def evaluate(self, prompt:str) -> Dict[str,Any] :
        #Mock evaluation logic
        is_toxic = "bad_word" in prompt.lower()
        return {
            "evaluator":self.name,
            "version":self.evaluator_version,
            "prompt":prompt,
            "passed":not is_toxic
        }
