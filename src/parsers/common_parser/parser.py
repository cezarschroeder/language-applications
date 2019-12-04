from abc import ABC, abstractmethod
from src.common.token import Token
from src.lexers.common_lexer.lexer import Lexer

class Parser(ABC):

    input_lexer: Lexer = None
    lookahead_token: Token = None

    def __init__(self, input_lexer: Lexer):
        self.input_lexer = input_lexer
        self.consume()

    def consume(self):
        self.lookahead_token = self.input_lexer.next_token()

    def match(self, token_type: int):
        if self.lookahead_token.token_type == token_type:
            self.consume()
        else:
            raise Exception('Error: Expecting: {}. Found: {}.'.format(self.input_lexer.get_token_name(token_type), self.lookahead_token))

