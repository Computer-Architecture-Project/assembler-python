from mock_lexer import Lexer
from my_parser import Parser

if __name__ == "__main__":
    lexer = Lexer()
    parser = Parser(lexer)