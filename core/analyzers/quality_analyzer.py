import ast
import builtins

from core.models import Issue


BUILTINS = set(dir(builtins))


def analyze_quality(tree):

    issues = []

    for node in ast.walk(tree):

        # -----------------------------------------
        # Bare except
        # -----------------------------------------

        if isinstance(node, ast.ExceptHandler):

            if node.type is None:

                issues.append(
                    Issue(
                        error_type="BareExcept",
                        category="Code Quality",
                        line=node.lineno,
                        column=node.col_offset + 1,
                        message="Bare except detected.",
                        confidence=98.0
                    )
                )

        # -----------------------------------------
        # Mutable default argument
        # -----------------------------------------

        if isinstance(
            node,
            (ast.FunctionDef, ast.AsyncFunctionDef)
        ):

            defaults = node.args.defaults

            for default in defaults:

                if isinstance(
                    default,
                    (ast.List, ast.Dict, ast.Set)
                ):

                    issues.append(
                        Issue(
                            error_type="MutableDefaultArgument",
                            category="Code Quality",
                            line=default.lineno,
                            column=default.col_offset + 1,
                            message=(
                                "Mutable object used as a "
                                "default function argument."
                            ),
                            confidence=97.0
                        )
                    )

        # -----------------------------------------
        # Built-in shadowing
        # -----------------------------------------

        if isinstance(node, ast.Name):

            if (
                isinstance(node.ctx, ast.Store)
                and node.id in BUILTINS
            ):

                issues.append(
                    Issue(
                        error_type="BuiltinShadowing",
                        category="Code Quality",
                        line=node.lineno,
                        column=node.col_offset + 1,
                        message=(
                            f"'{node.id}' shadows a Python built-in."
                        ),
                        confidence=95.0
                    )
                )

    return issues