"""
🎯 Challenge: TextSummarizer Configuration & Utility
You are building a text summarization module for an AI workflow. You need to create a TextSummarizer class that holds model configuration and utility tools.

Requirements:
__init__: Accepts model_name (str) and max_summary_length (int).

@classmethod (preset_fast):

Takes no arguments (besides cls).

Returns a new instance configured with model_name="gpt-4o-mini" and max_summary_length=100.

@staticmethod (clean_whitespace):

Takes a string text.

Returns the string cleaned up: stripped of leading/trailing whitespace and converted to lowercase.

(Does not touch self or cls).
"""


class TextSummarizer:
    def __init__(self, max_summary_length: int, model_name: str):
        self.max_summary_length = max_summary_length
        self.model_name = model_name

    @classmethod
    def preset_fast(cls):
        return cls(model_name="gpt-4o-mini", max_summary_length=100)

    @staticmethod
    def clean_whitespace(mystring: str):
        return mystring.strip().lower()
