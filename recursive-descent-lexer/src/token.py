class Token:

    tokenType: int
    tokenName: str
    tokenValue: str

    def __init__(self, tokenType: int, tokenName: str, tokenText: str):
        self.tokenType = tokenType
        self.tokenName = tokenName
        self.tokenText = tokenText

    def __str__(self):
        return '< {} , {} >'.format(self.tokenName, self.tokenText)