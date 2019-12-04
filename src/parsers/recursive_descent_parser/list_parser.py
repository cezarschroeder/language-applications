from src.common.token import Token
from src.lexers.common_lexer.lexer import Lexer
from src.lexers.recursive_descent_lexer.list_lexer import ListLexer
from src.parsers.common_parser.parser import Parser

class ListParser(Parser):

    def __init__(self, input_lexer: Lexer):
        super().__init__(input_lexer)

    def parse_list(self):
        self.match(self.input_lexer.LBRACK)
        self.elements()
        self.match(self.input_lexer.RBRACK)

    def elements(self):
        self.element()
        while self.lookahead_token.token_type == self.input_lexer.COMMA:
            self.match(self.input_lexer.COMMA)
            self.element()
    
    def element(self):
        if self.lookahead_token.token_type == self.input_lexer.NAME:
            self.match(self.input_lexer.NAME)
        elif self.lookahead_token.token_type == self.input_lexer.LBRACK:
            self.parse_list()
        else:
            raise Exception('Error: Expecting NAME or LIST. Found: {}.'.format(self.lookahead_token))
    