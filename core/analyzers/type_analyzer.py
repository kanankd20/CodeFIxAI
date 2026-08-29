import ast

from core.models import Issue


def get_simple_type(node):

    if isinstance(node, ast.Constant):

        if isinstance(node.value, bool):
            return "bool"

        if isinstance(node.value, int):
            return "int"

        if isinstance(node.value, float):
            return "float"

        if isinstance(node.value, str):
            return "str"

        if node.value is None:
            return "None"

    if isinstance(node, ast.List):
        return "list"

    if isinstance(node, ast.Tuple):
        return "tuple"

    if isinstance(node, ast.Dict):
        return "dict"

    if isinstance(node, ast.Set):
        return "set"

    return None


def analyze_types(tree):

    issues = []

    variable_types = {}

    for node in ast.walk(tree):

        if isinstance(node, ast.Assign):

            value_type = get_simple_type(node.value)

            if value_type:

                for target in node.targets:

                    if isinstance(target, ast.Name):

                        variable_types[target.id] = value_type

        if isinstance(node, ast.BinOp):

            left_type = get_simple_type(node.left)

            right_type = get_simple_type(node.right)

            if (
                left_type == "str"
                and right_type in {"int", "float"}
            ):

                issues.append(
                    Issue(
                        error_type="PossibleTypeError",
                        category="Type",
                        line=node.lineno,
                        column=node.col_offset + 1,
                        message=(
                            "String and numeric values are "
                            "being combined."
                        ),
                        confidence=94.0
                    )
                )

    return issues