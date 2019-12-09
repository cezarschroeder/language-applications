from src.common.token import Token
from src.lexers.common_lexer.lexer import Lexer
from src.lexers.recursive_descent_lexer.list_lexer import ListLexer
from src.parsers.common_parser.krd_parser import KRDParser

class KRDListParser(KRDParser):

    def __init__(self, input_lexer: ListLexer, k_value: int):
        super().__init__(input_lexer, k_value)

    def parse_list(self):
        self.match(self.input_lexer.LBRACK)
        self.elements()
        self.match(self.input_lexer.RBRACK)

    def elements(self):
        self.element()
        while self.get_lookahead_token_type(1) == self.input_lexer.COMMA:
            self.match(self.input_lexer.COMMA)
            self.element()

    def element(self):
        if self.get_lookahead_token_type(1) == self.input_lexer.NAME and self.get_lookahead_token_type(2) == self.input_lexer.EQUALS:
            self.match(self.input_lexer.NAME)
            self.match(self.input_lexer.EQUALS)
            self.match(self.input_lexer.NAME)
        elif self.get_lookahead_token_type(1) == self.input_lexer.NAME:
            self.match(self.input_lexer.NAME)
        elif self.get_lookahead_token_type(1) == self.input_lexer.LBRACK:
            self.parse_list()
        else:
            raise Exception('Error: Expecting NAME or LIST. Found: {}.'.format(self.get_lookahead_token(1)))