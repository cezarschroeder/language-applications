class Token:

    token_type: int
    token_name: str
    token_value: str

    def __init__(self, token_type: int, token_name: str, token_text: str):
        self.token_type = token_type
        self.token_name = token_name
        self.token_text = token_text

    def __str__(self):
        return '< {} , {} >'.format(self.token_name, self.token_text)