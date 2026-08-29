import ast

from core.models import Issue


class ControlFlowAnalyzer(ast.NodeVisitor):

    def __init__(self):

        self.loop_depth = 0
        self.issues = []

    def visit_For(self, node):

        self.loop_depth += 1

        self.generic_visit(node)

        self.loop_depth -= 1

    def visit_While(self, node):

        self.loop_depth += 1

        self.generic_visit(node)

        self.loop_depth -= 1

    def visit_Break(self, node):

        if self.loop_depth == 0:

            self.issues.append(
                Issue(
                    error_type="BreakOutsideLoop",
                    category="Control Flow",
                    line=node.lineno,
                    column=node.col_offset + 1,
                    message=(
                        "'break' is used outside a loop."
                    ),
                    confidence=99.0
                )
            )

    def visit_Continue(self, node):

        if self.loop_depth == 0:

            self.issues.append(
                Issue(
                    error_type="ContinueOutsideLoop",
                    category="Control Flow",
                    line=node.lineno,
                    column=node.col_offset + 1,
                    message=(
                        "'continue' is used outside a loop."
                    ),
                    confidence=99.0
                )
            )


def analyze_control_flow(tree):

    visitor = ControlFlowAnalyzer()

    visitor.visit(tree)

    return visitor.issues