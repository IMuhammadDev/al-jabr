class Interpreter:
    def __init__(self, tree):
        self.tree = tree
        self.env = {}

    def eval(self, node):
        if node.type == "Program":
            for child in node.children:
                self.eval(child)
        elif node.type == "Statement":
            id_node = node.children[0]
            expr_node = node.children[2]
            value = self.eval(expr_node)
            self.env[id_node.value] = value
        elif node.type == "Expression":
            left = self.eval(node.children[0])
            if len(node.children) > 1:
                op = node.children[1].value
                right = self.eval(node.children[2])
                if op == "+":
                    return left + right
                elif op == "-":
                    return left - right
                elif op == "*":
                    return left * right
                elif op == "/":
                    return left / right
            else:
                return left
        elif node.type == "Term":
            if node.children[0].type == "Number":
                return node.children[0].value
            elif node.children[0].type == "Identifier":
                return self.env[node.children[0].value]
        return None
