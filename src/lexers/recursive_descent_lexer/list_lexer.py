from src.lexers.common_lexer.lexer import Lexer
from src.common.token import Token

class ListLexer(Lexer):

    # Token Type Definitions
    NAME: int = 2
    COMMA: int = 3
    LBRACK: int = 4
    RBRACK: int = 5

    # Token Text (Name) Definitions
    token_names: list = ['N/A', 'EOF', 'NAME', 'COMMA', 'LBRACK', 'RBRACK']
    white_space_chars: list = set([' ', '\t', '\n', '\r'])
    
    def __init__(self, input_string: str):
        super().__init__(input_string)
    
    def get_token_name(self, token_type: int):
        return self.token_names[token_type]
    
    def next_token(self):
        while self.current_char != self.EOF:
            if self.current_char in self.white_space_chars:
                self.consume()
            elif self.current_char == ',':
                self.consume()
                return Token(self.COMMA, self.get_token_name(self.COMMA), ',')
            elif self.current_char == '[':
                self.consume()
                return Token(self.LBRACK, self.get_token_name(self.LBRACK), '[')
            elif self.current_char == ']':
                self.consume()
                return Token(self.RBRACK, self.get_token_name(self.RBRACK), ']')
            else:
                if self.is_letter():
                    return self.process_name_token()
                print(self.current_char)
                raise Exception('Error: Invalid Character: {}'.format(self.current_char))
        return Token(self.EOF_TYPE, self.get_token_name(self.EOF_TYPE), '<EOF>')
    
    def is_letter(self):
        char = ord(self.current_char)
        lower_case_range = range(ord('a'), ord('z'))
        upper_case_range = range(ord('A'), ord('Z'))
        return ((char in lower_case_range) or (char in upper_case_range))

    def process_name_token(self):
        string_buffer = self.current_char
        self.consume()
        while self.is_letter():
            string_buffer += self.current_char
            self.consume()
        return Token(self.NAME, self.get_token_name(self.NAME), string_buffer)
        