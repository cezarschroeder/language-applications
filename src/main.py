import sys
import argparse
from src.common.token import Token
from src.lexers.common_lexer.lexer import Lexer
from src.lexers.recursive_descent_lexer.list_lexer import ListLexer
from src.parsers.common_parser.parser import Parser
from src.parsers.recursive_descent_parser.list_parser import ListParser
from src.parsers.recursive_descent_parser.krd_list_parser import KRDListParser

def main(argv):
    cli_parser = argparse.ArgumentParser(description='Some language application demos (e.g. lexers, parsers, semantic analyzers, interpreters, and generators).')
    cli_parser.add_argument('--lexer', nargs=1, type=str, help='calls LL(1) recursive-descent lexer with the provided input')
    cli_parser.add_argument('--parser', nargs=1, type=str, help='calls LL(1) recursive-descent parser with the provided input')
    cli_parser.add_argument('--krdparser', nargs=1, type=str, help='calls LL(k) recursive-descent parser with the provided input')
    cli_parser.add_argument('--kvalue', type=int, default=2, help='value of k for the LL(k) recursive-descent parser')
    parsed_args = cli_parser.parse_args()
    if parsed_args.lexer is not None:
        recursive_descent_lexer(parsed_args.lexer[0])
    elif parsed_args.parser is not None:
        recursive_descent_parser(parsed_args.parser[0])
    elif parsed_args.krdparser is not None:
        k_recursive_descent_parser(parsed_args.krdparser[0], parsed_args.kvalue)

def recursive_descent_lexer(input_string: str):
    list_lexer = ListLexer(input_string)
    token = list_lexer.next_token()
    while token.token_type != list_lexer.EOF_TYPE:
        print(token)
        token = list_lexer.next_token()
    print(token) # EOF

def recursive_descent_parser(input_string: str):
    list_lexer = ListLexer(input_string)
    list_parser = ListParser(list_lexer)
    list_parser.parse_list()
    print('Input was successfully parsed.')

def k_recursive_descent_parser(input_string: str, k_value: int):
    assert k_value > 0, 'Error: K value must be greater than zero.'
    list_lexer = ListLexer(input_string)
    krd_list_parser = KRDListParser(list_lexer, k_value)
    krd_list_parser.parse_list()
    print('Input was successfully parsed.')

if __name__ == '__main__':
    main(sys.argv)