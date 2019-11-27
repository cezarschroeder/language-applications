from abc import ABC, abstractmethod

class Lexer(ABC):

    EOF: str = '<EOF>'
    EOF_TYPE: int = 1
    inputString: str
    currentPosition: int = 0
    currentChar: str

    def __init__(self, inputString: str):
        self.inputString = inputString
        currentChar = inputString[currentPosition]

    def consume(self):
        currentPosition += 1
        if currentPosition >= len(self.inputString):
            currentChar = self.EOF
        else:
            currentChar = self.inputString[currentPosition]

    def match(self, char: str):
        if self.currentChar == char:
            self.consume()
        else:
            raise Exception('Error: Expecting: {}. Found: {}.'.format(char, currentChar))

    @abstractmethod
    def nextToken(self):
        pass

    @abstractmethod
    def getTokenName(self, tokenType: int):
        pass
