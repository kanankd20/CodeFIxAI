import ast

from core.models import Issue


def analyze_syntax(code):
    """
    Detect Python syntax errors without executing the code.
    """

    try:
        tree = ast.parse(
            code,
            filename="<CodeFixAI>"
        )

        return tree, []

    except SyntaxError as error:

        issue = Issue(
            error_type="SyntaxError",
            category="Syntax",
            line=error.lineno,
            column=error.offset,
            message=error.msg or "Invalid Python syntax.",
            confidence=99.0
        )

        return None, [issue]