from core.models import Issue


CATEGORY_MAP = {

    # Syntax
    "SyntaxError": "Syntax",
    "IndentationError": "Syntax",

    # Names
    "UndefinedName": "Name",
    "BuiltinShadowing": "Name",

    # Types
    "PossibleTypeError": "Type",

    # Security
    "DangerousFunction": "Security",

    # Code Quality
    "MutableDefaultArgument": "Code Quality",
    "BareExcept": "Code Quality",

    # Control Flow
    "BreakOutsideLoop": "Control Flow",
    "ContinueOutsideLoop": "Control Flow",

    # Future categories
    "ImportError": "Import",
    "UnusedImport": "Import",
    "DivisionByZero": "Runtime",
    "InfiniteLoop": "Logic",
}


def classify_issue(issue: Issue) -> Issue:
    """
    Assign a standardized category to an issue.
    """

    category = CATEGORY_MAP.get(
        issue.error_type,
        issue.category
    )

    issue.category = category

    return issue


def classify_issues(issues):

    classified = []

    for issue in issues:

        classified_issue = classify_issue(issue)

        classified.append(
            classified_issue
        )

    return classified