'''🎯 Challenge: The BaseGuardrail Contract
In AI safety systems, guardrail modules check whether input prompts or output responses satisfy safety rules (like PII masking, toxicity checks, or topic compliance).

You need to implement a concrete LengthGuardrail class that enforces an Abstract Base Class interface.

Requirements:
Inherit from BaseGuardrail (provided below).

Implement the mandatory abstract property rule_name:

Return the string "Length Limit Check".

Implement the mandatory abstract method validate(self, text: str) -> bool:

Check if len(text) is less than or equal to self.max_length.

Return True if it passes, False if it exceeds max_length.'''


from abc import ABC, abstractmethod

# 1. THE ABSTRACT CONTRACT
class BaseGuardrail(ABC):
    @property
    @abstractmethod
    def rule_name(self) -> str:
        """Name of the guardrail rule."""
        pass

    @abstractmethod
    def validate(self, text: str) -> bool:
        """Validates input text against safety rules."""
        pass


# 2. YOUR SUBCLASS TO IMPLEMENT
class LengthGuardrail(BaseGuardrail):
    def __init__(self, max_length: int = 50):
        self.max_length = max_length

    # TODO 1: Implement the @property 'rule_name'
    @property
    def rule_name(self):
        return 'Length limit check'

    # TODO 2: Implement the 'validate' method
    def validate(self, text) -> bool:
        return len(text) <= self.max_length