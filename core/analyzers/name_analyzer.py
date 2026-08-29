import ast
import builtins

from core.models import Issue


BUILTINS = set(dir(builtins))


class NameAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.defined = set()
        self.used = []

    def visit_FunctionDef(self, node):

        self.defined.add(node.name)

        for arg in node.args.args:
            self.defined.add(arg.arg)

        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):

        self.defined.add(node.name)

        for arg in node.args.args:
            self.defined.add(arg.arg)

        self.generic_visit(node)

    def visit_ClassDef(self, node):

        self.defined.add(node.name)

        self.generic_visit(node)

    def visit_Name(self, node):

        if isinstance(node.ctx, ast.Store):

            self.defined.add(node.id)

        elif isinstance(node.ctx, ast.Load):

            self.used.append(node)

        self.generic_visit(node)


def analyze_names(tree):

    visitor = NameAnalyzer()

    visitor.visit(tree)

    issues = []

    for node in visitor.used:

        if node.id not in visitor.defined:

            if node.id not in BUILTINS:

                issues.append(
                    Issue(
                        error_type="UndefinedName",
                        category="Name",
                        line=node.lineno,
                        column=node.col_offset + 1,
                        message=(
                            f"Name '{node.id}' is not defined."
                        ),
                        confidence=90.0
                    )
                )

    return issues