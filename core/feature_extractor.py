"""
=============================================================
                       CODEFIX AI
                   FEATURE EXTRACTOR
=============================================================

Purpose:
    Convert Python source code into useful features that can
    later be used by the Machine Learning classifier.

Current language:
    Python

Features extracted:
    - Number of lines
    - Number of characters
    - Number of functions
    - Number of classes
    - Number of imports
    - Number of loops
    - Number of conditionals
    - Number of try/except blocks
    - Number of dangerous functions
    - Number of variables
    - Number of comments
    - Number of strings
    - Number of numeric constants
    - Syntax validity
    - AST node count
    - Maximum nesting depth

=============================================================
"""

import ast
import re


# ============================================================
# DANGEROUS FUNCTIONS
# ============================================================

DANGEROUS_FUNCTIONS = {
    "eval",
    "exec",
    "compile",
    "__import__",
}


# ============================================================
# KEYWORD GROUPS
# ============================================================

LOOP_KEYWORDS = {
    "for",
    "while",
}


CONDITIONAL_KEYWORDS = {
    "if",
    "elif",
    "else",
}


# ============================================================
# SAFE AST PARSE
# ============================================================

def parse_code(code):

    """
    Try to parse Python source code.

    Returns:
        AST tree if valid.
        None if syntax is invalid.
    """

    try:

        return ast.parse(code)

    except SyntaxError:

        return None


# ============================================================
# BASIC TEXT FEATURES
# ============================================================

def count_lines(code):

    """Count non-empty lines."""

    return sum(
        1
        for line in code.splitlines()
        if line.strip()
    )


def count_characters(code):

    """Count total characters."""

    return len(code)


def count_comments(code):

    """Count Python comment lines."""

    count = 0

    for line in code.splitlines():

        stripped = line.strip()

        if stripped.startswith("#"):

            count += 1

    return count


def count_strings(code):

    """Approximate number of quoted strings."""

    pattern = r"""(['"])(?:\\.|(?!\1).)*\1"""

    return len(
        re.findall(
            pattern,
            code
        )
    )


# ============================================================
# AST FEATURES
# ============================================================

def count_ast_nodes(tree):

    """Count AST nodes."""

    if tree is None:

        return 0

    return sum(
        1
        for _ in ast.walk(tree)
    )


def count_functions(tree):

    """Count function definitions."""

    if tree is None:

        return 0

    return sum(
        1
        for node in ast.walk(tree)
        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
            )
        )
    )


def count_classes(tree):

    """Count classes."""

    if tree is None:

        return 0

    return sum(
        1
        for node in ast.walk(tree)
        if isinstance(
            node,
            ast.ClassDef
        )
    )


def count_imports(tree):

    """Count import statements."""

    if tree is None:

        return 0

    return sum(
        1
        for node in ast.walk(tree)
        if isinstance(
            node,
            (
                ast.Import,
                ast.ImportFrom,
            )
        )
    )


def count_loops(tree):

    """Count for and while loops."""

    if tree is None:

        return 0

    return sum(
        1
        for node in ast.walk(tree)
        if isinstance(
            node,
            (
                ast.For,
                ast.While,
                ast.AsyncFor,
            )
        )
    )


def count_conditionals(tree):

    """Count if statements."""

    if tree is None:

        return 0

    return sum(
        1
        for node in ast.walk(tree)
        if isinstance(
            node,
            ast.If
        )
    )


def count_try_blocks(tree):

    """Count try blocks."""

    if tree is None:

        return 0

    return sum(
        1
        for node in ast.walk(tree)
        if isinstance(
            node,
            ast.Try
        )
    )


def count_variables(tree):

    """Count variable assignments."""

    if tree is None:

        return 0

    return sum(
        1
        for node in ast.walk(tree)
        if isinstance(
            node,
            (
                ast.Assign,
                ast.AnnAssign,
                ast.AugAssign,
            )
        )
    )


def count_numeric_constants(tree):

    """Count numeric constants."""

    if tree is None:

        return 0

    count = 0

    for node in ast.walk(tree):

        if isinstance(
            node,
            ast.Constant
        ):

            if isinstance(
                node.value,
                (
                    int,
                    float,
                    complex,
                )
            ):

                count += 1

    return count


# ============================================================
# DANGEROUS FUNCTION COUNT
# ============================================================

def count_dangerous_functions(tree):

    """
    Count calls to dangerous functions such as eval and exec.
    """

    if tree is None:

        return 0

    count = 0

    for node in ast.walk(tree):

        if isinstance(
            node,
            ast.Call
        ):

            if isinstance(
                node.func,
                ast.Name
            ):

                if node.func.id in DANGEROUS_FUNCTIONS:

                    count += 1

    return count


# ============================================================
# MAXIMUM NESTING DEPTH
# ============================================================

def calculate_nesting_depth(tree):

    """
    Calculate approximate maximum nesting depth.
    """

    if tree is None:

        return 0


    def depth(node, current_depth):

        maximum = current_depth

        for child in ast.iter_child_nodes(node):

            child_depth = depth(
                child,
                current_depth + 1
            )

            maximum = max(
                maximum,
                child_depth
            )

        return maximum


    return depth(
        tree,
        0
    )


# ============================================================
# SYNTAX VALIDITY
# ============================================================

def syntax_valid(code):

    """Return 1 if syntax is valid, otherwise 0."""

    try:

        ast.parse(code)

        return 1

    except SyntaxError:

        return 0


# ============================================================
# MAIN FEATURE EXTRACTION
# ============================================================

def extract_features(code):

    """
    Extract all features from Python source code.

    Returns:
        Dictionary containing numerical features.
    """

    if code is None:

        code = ""


    code = str(code)


    tree = parse_code(
        code
    )


    features = {

        # -----------------------------------------------
        # TEXT FEATURES
        # -----------------------------------------------

        "line_count":
            count_lines(code),

        "character_count":
            count_characters(code),

        "comment_count":
            count_comments(code),

        "string_count":
            count_strings(code),


        # -----------------------------------------------
        # AST FEATURES
        # -----------------------------------------------

        "ast_node_count":
            count_ast_nodes(tree),

        "function_count":
            count_functions(tree),

        "class_count":
            count_classes(tree),

        "import_count":
            count_imports(tree),

        "loop_count":
            count_loops(tree),

        "conditional_count":
            count_conditionals(tree),

        "try_count":
            count_try_blocks(tree),

        "variable_count":
            count_variables(tree),

        "numeric_constant_count":
            count_numeric_constants(tree),


        # -----------------------------------------------
        # SECURITY
        # -----------------------------------------------

        "dangerous_function_count":
            count_dangerous_functions(tree),


        # -----------------------------------------------
        # COMPLEXITY
        # -----------------------------------------------

        "nesting_depth":
            calculate_nesting_depth(tree),


        # -----------------------------------------------
        # SYNTAX
        # -----------------------------------------------

        "syntax_valid":
            syntax_valid(code),
    }


    return features


# ============================================================
# DATAFRAME FEATURE EXTRACTION
# ============================================================

def extract_dataset_features(df):

    """
    Extract features from every code sample in a DataFrame.

    Returns:
        pandas DataFrame containing numerical features.
    """

    import pandas as pd


    feature_rows = []


    for code in df["code"]:

        features = extract_features(
            code
        )

        feature_rows.append(
            features
        )


    return pd.DataFrame(
        feature_rows
    )


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print()

    print("=" * 70)

    print(
        "                    CODEFIX AI"
    )

    print(
        "                  FEATURE EXTRACTOR"
    )

    print("=" * 70)


    test_code = """
def calculate_total(items=[]):

    total = 0

    for item in items:

        if item > 0:

            total += item

    eval("print(total)")

    return total
"""


    print()

    print(
        "TEST SOURCE CODE"
    )

    print(
        "-" * 50
    )

    print(
        test_code
    )


    features = extract_features(
        test_code
    )


    print()

    print(
        "EXTRACTED FEATURES"
    )

    print(
        "-" * 50
    )


    for name, value in features.items():

        print(
            f"{name:<30} : {value}"
        )


    print()

    print("=" * 70)

    print(
        "              FEATURE EXTRACTION COMPLETE"
    )

    print("=" * 70)

    print()