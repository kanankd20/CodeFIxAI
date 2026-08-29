import ast

from core.models import Issue


DANGEROUS_FUNCTIONS = {
    "eval",
    "exec",
}


def analyze_security(tree):

    issues = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Call):

            if isinstance(node.func, ast.Name):

                function_name = node.func.id

                if function_name in DANGEROUS_FUNCTIONS:

                    issues.append(
                        Issue(
                            error_type="DangerousFunction",
                            category="Security",
                            line=node.lineno,
                            column=node.col_offset + 1,
                            message=(
                                f"Dangerous function "
                                f"'{function_name}()' detected."
                            ),
                            confidence=96.0
                        )
                    )

    return issues