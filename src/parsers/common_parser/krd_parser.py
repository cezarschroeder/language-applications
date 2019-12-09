from abc import ABC, abstractmethod
from src.common.token import Token
from src.lexers.common_lexer.lexer import Lexer

class KRDParser(ABC):

    input_lexer: Lexer = None
    lookahead_tokens: list = []
    k_value: int = 0
    current_position: int = 0

    def __init__(self, input_lexer: Lexer, k_value: int):
        self.input_lexer = input_lexer
        self.k_value = k_value
        for i in range(self.k_value):
            self.lookahead_tokens.append(Token(0,'',''))
            self.consume()

    def consume(self):
        self.lookahead_tokens[self.current_position] = self.input_lexer.next_token()
        self.current_position = (self.current_position + 1) % self.k_value

    def get_lookahead_token_type(self, lookahead_token_position: int):
        assert lookahead_token_position > 0, 'Error: Lookahead token position must be greater than zero.'
        token: Token = self.get_lookahead_token(lookahead_token_position)
        return token.token_type

    def get_lookahead_token(self, lookahead_token_position: int):
        assert lookahead_token_position > 0, 'Error: Lookahead token position must be greater than zero.'
        return self.lookahead_tokens[(self.current_position + lookahead_token_position - 1) % self.k_value]

    def match(self, token_type: int):
        if self.get_lookahead_token_type(1) == token_type:
            self.consume()
        else:
            token: Token = self.get_lookahead_token(1)
            raise Exception('Error: Expecting: {}. Found: {}.'.format(self.input_lexer.get_token_name(token_type), self.input_lexer.get_token_name(token.token_type)))
