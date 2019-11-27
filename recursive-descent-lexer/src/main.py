import sys
from token import Token
from lexer import Lexer
from list_lexer import ListLexer

def main(argv):
    listLexer = ListLexer(argv[1])
    token: Token = listLexer.nextToken()
    while token.tokenType != listLexer.EOF_TYPE:
        print(token)
        token = listLexer.nextToken()
    print(token) # EOF

if __name__ == '__main__':
    main(sys.argv)