from abc import ABC, abstractmethod
from src.common.token import Token
from src.lexers.common_lexer.lexer import Lexer

class BacktrackingParser(ABC):

    input_lexer: Lexer = None
    index_markers: list = []
    lookahead_tokens: list = []
    current_position: int = 0

    # Basic Parsing Infrastructure
    def __init__(self, input_lexer: Lexer):
        pass

    def consume(self):
        pass

    def match(self, token_type: int):
        pass

    # LL(k)-ish Recursive-Descent Parsing Infrastructure
    def get_lookahead_token(self, lookahead_token_position: int):
        pass

    def get_lookahead_token_type(self, lookahead_token_position: int):
        pass

    # Backtracking Parsing Auxiliary Infrastructure
    def is_speculating(self):
        pass

    def mark(self):
        pass

    def release(self):
        pass

    def seek(self, index: int):
        pass

    def sync(self, lookahead_token_position: int):
        pass

    def fill(self, lookahead_token_position: int):
        pass