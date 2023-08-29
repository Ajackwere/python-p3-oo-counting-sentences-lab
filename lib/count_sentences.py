class MyString:
    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = self.value.split('.')
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)


string = MyString("This is a string! It has three sentences. Right?")
