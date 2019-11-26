class Token:

    tokenType: int
    tokenText: str

    def __init__(self, tokenType, tokenText):
        self.tokenType = tokenType
        self.tokenText = tokenText

    def __str__(self):
        return '< {} , {} >'.format(self.tokenType, self.tokenText)