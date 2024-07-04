class Node:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self, level=0):
        ret = (
            "\t" * level
            + repr(self.type)
            + (": " + repr(self.value) if self.value else "")
            + "\n"
        )
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


def parse(tokens):
    tokens = iter(tokens)
    current_token = next(tokens, None)

    def accept(expected_type):
        nonlocal current_token
        if current_token and current_token[0] == expected_type:
            value = current_token[1]
            current_token = next(tokens, None)
            return value
        return None

    def expect(expected_type):
        value = accept(expected_type)
        if value is None:
            raise SyntaxError(f"Expected {expected_type}")
        return value

    def expression():
        node = Node("Expression")
        term_node = term()
        node.add_child(term_node)
        while current_token and current_token[0] == "OP":
            op_node = Node("Operator", accept("OP"))
            node.add_child(op_node)
            term_node = term()
            node.add_child(term_node)
        return node

    def term():
        node = Node("Term")
        number = accept("NUMBER")
        if number is not None:
            node.add_child(Node("Number", number))
        else:
            id = accept("ID")
            if id is not None:
                node.add_child(Node("Identifier", id))
            else:
                raise SyntaxError(f"Expected NUMBER or ID")
        return node

    def statement():
        node = Node("Statement")
        id_node = Node("Identifier", expect("ID"))
        node.add_child(id_node)
        node.add_child(Node("Assign", expect("ASSIGN")))
        expr_node = expression()
        node.add_child(expr_node)
        expect("END")
        return node

    root = Node("Program")
    while current_token:
        stmt_node = statement()
        root.add_child(stmt_node)
    return root


# Test the parser
if __name__ == "__main__":
    from lexer import lex

    code = "a = 5 + 3;\nb = a * 2;"
    tokens = list(lex(code))
    syntax_tree = parse(tokens)
    print(syntax_tree)
