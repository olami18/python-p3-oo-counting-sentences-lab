#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=None):
        if isinstance(value, str):
            self.value = value
        else:
            print("The value must be a string.")
            self.value = ""

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        if not self.value:
            return 0
        sentences = re.split(r'[.!?]', self.value)
        non_empty_sentences = [s.strip() for s in sentences if s.strip()]
        return len(non_empty_sentences)

    
