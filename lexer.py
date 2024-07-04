import re

TOKEN_SPECIFICATION = [
    ("NUMBER", r"\d+"),  # Integer or decimal number
    ("ASSIGN", r"="),  # Assignment operator
    ("END", r";"),  # Statement terminator
    ("ID", r"[A-Za-z]+"),  # Identifiers
    ("OP", r"[+\-*/]"),  # Arithmetic operators
    ("SKIP", r"[ \t]+"),  # Skip over spaces and tabs
    ("NEWLINE", r"\n"),  # Line endings
]

token_regex = "|".join("(?P<%s>%s)" % pair for pair in TOKEN_SPECIFICATION)


def lex(characters):
    for mo in re.finditer(token_regex, characters):
        kind = mo.lastgroup
        value = mo.group()
        if kind == "NUMBER":
            value = int(value)
        elif kind == "NEWLINE":
            continue
        elif kind == "SKIP":
            continue
        yield kind, value


# Test the lexer
if __name__ == "__main__":
    code = "a = 5 + 3;\nb = a * 2;"
    tokens = list(lex(code))
    for token in tokens:
        print(token)
