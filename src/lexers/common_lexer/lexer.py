from abc import ABC, abstractmethod

class Lexer(ABC):

    EOF = '<EOF>'
    EOF_TYPE = 1
    input_string = ''
    current_position = 0
    current_char = ''

    def __init__(self, input_string):
        self.input_string = input_string
        self.current_char = input_string[self.current_position]

    def consume(self):
        self.current_position += 1
        if self.current_position >= len(self.input_string):
            self.current_char = self.EOF
        else:
            self.current_char = self.input_string[self.current_position]

    def match(self, char):
        if self.current_char == char:
            self.consume()
        else:
            raise Exception('Error: Expecting: {}. Found: {}.'.format(char, self.current_char))

    @abstractmethod
    def next_token(self):
        pass

    @abstractmethod
    def get_token_name(self, token_type):
        pass
