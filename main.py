from lexer import lex
from parser import parse
from interpreter import Interpreter


def main():
    code = """
    a = 5 + 3;
    b = a * 2;
    """
    tokens = list(lex(code))
    print("Tokens:")
    for token in tokens:
        print(token)

    syntax_tree = parse(tokens)
    print("\nSyntax Tree:")
    print(syntax_tree)

    interpreter = Interpreter(syntax_tree)
    interpreter.eval(syntax_tree)
    print("\nEnvironment:")
    print(interpreter.env)


if __name__ == "__main__":
    main()
