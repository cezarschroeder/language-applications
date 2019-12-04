import sys
import argparse
from src.common.token import Token
from src.lexers.common_lexer.lexer import Lexer
from src.lexers.recursive_descent_lexer.list_lexer import ListLexer
from src.parsers.common_parser.parser import Parser
from src.parsers.recursive_descent_parser.list_parser import ListParser

def main(argv):
    cli_parser = argparse.ArgumentParser(description='Some language application demos (e.g. lexers, parsers, semantic analyzers, interpreters, and generators).')
    cli_parser.add_argument('--lexer', nargs=1, type=str, help='calls lexer with the provided input')
    cli_parser.add_argument('--parser', nargs=1, type=str, help='calls parser with the provided input')
    parsed_args = cli_parser.parse_args()
    if parsed_args.lexer is not None:
        recursive_descent_lexer(parsed_args.lexer[0])
    elif parsed_args.parser is not None:
        recursive_descent_parser(parsed_args.parser[0])

def recursive_descent_lexer(input_string):
    list_lexer = ListLexer(input_string)
    token = list_lexer.next_token()
    while token.token_type != list_lexer.EOF_TYPE:
        print(token)
        token = list_lexer.next_token()
    print(token) # EOF
    pass

def recursive_descent_parser(input_string):
    list_lexer = ListLexer(input_string)
    list_parser = ListParser(list_lexer)
    list_parser.parse_list()
    print('Input was successfully parsed.')
    pass

if __name__ == '__main__':
    main(sys.argv)