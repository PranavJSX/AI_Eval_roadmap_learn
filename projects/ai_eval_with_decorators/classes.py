from decorators import *

class PromptLengthEvaluator:
    def __init__(self,max_allowed_characters):
        self.max_allowed_characters = max_allowed_characters

    @cache_response
    @log_eval_run
    def __call__(self, prompt:str):
        time.sleep(0.3)

        char_count = len(prompt)
        is_valid = char_count<=self.max_allowed_characters

        return {
            "prompt":prompt,
            "char_count":char_count,
            "max_allowed":self.max_allowed_characters,
            "passed":is_valid
        }