from lexer import Lexer
from token import Token

class ListLexer(Lexer):

    # Token Type Definitions
    NAME: int = 2
    COMMA: int = 3
    LBRACK: int = 4
    RBRACK: int = 5

    # Token Text (Name) Definitions
    tokenNames: list = ['N/A', 'EOF', 'NAME', 'COMMA', 'LBRACK', 'RBRACK']
    whiteSpaceChars = set([' ', '\t', '\n', '\r'])
    
    def __init__(self, inputString: str):
        super().__init__(inputString)
    
    def getTokenName(self, tokenType):
        return self.tokenNames[tokenType]
    
    def nextToken(self):
        while self.currentChar != self.EOF:
            if self.currentChar in self.whiteSpaceChars:
                self.consume()
            elif self.currentChar == ',':
                self.consume()
                return Token(self.COMMA, self.getTokenName(self.COMMA), ',')
            elif self.currentChar == '[':
                self.consume()
                return Token(self.LBRACK, self.getTokenName(self.LBRACK), '[')
            elif self.currentChar == ']':
                self.consume()
                return Token(self.RBRACK, self.getTokenName(self.RBRACK), ']')
            else:
                if self.isLetter():
                    return self.NameToken()
                print(self.currentChar)
                raise Exception('Error: Invalid Character: {}'.format(self.currentChar))
        return Token(self.EOF_TYPE, self.getTokenName(self.EOF_TYPE), '<EOF>')
    
    def isLetter(self):
        char = ord(self.currentChar)
        lowerCaseRange = range(ord('a'), ord('z'))
        upperCaseRange = range(ord('A'), ord('Z'))
        return ((char in lowerCaseRange) or (char in upperCaseRange))

    def NameToken(self):
        stringBuffer = self.currentChar
        self.consume()
        while self.isLetter():
            stringBuffer += self.currentChar
            self.consume()
        return Token(self.NAME, self.getTokenName(self.NAME), stringBuffer)
        