#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        if not self.value:
            return 0
        
        value_without_exclamation = self.value.replace('!', '.')
        value_without_question = value_without_exclamation.replace('?', '.')

        sentences = value_without_question.split('.')

        count = sum(1 for sentence in sentences if sentence.strip())

        return count


