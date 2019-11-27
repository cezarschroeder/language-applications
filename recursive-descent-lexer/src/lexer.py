from abc import ABC, abstractmethod

class Lexer(ABC):

    EOF: str = '<EOF>'
    EOF_TYPE: int = 1
    inputString: str = ''
    currentPosition: int = 0
    currentChar: str = ''

    def __init__(self, inputString: str):
        self.inputString = inputString
        self.currentChar = inputString[self.currentPosition]

    def consume(self):
        self.currentPosition += 1
        if self.currentPosition >= len(self.inputString):
            self.currentChar = self.EOF
        else:
            self.currentChar = self.inputString[self.currentPosition]

    def match(self, char: str):
        if self.currentChar == char:
            self.consume()
        else:
            raise Exception('Error: Expecting: {}. Found: {}.'.format(char, self.currentChar))

    @abstractmethod
    def nextToken(self):
        pass

    @abstractmethod
    def getTokenName(self, tokenType: int):
        pass
