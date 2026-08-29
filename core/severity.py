from core.models import Issue


SEVERITY_RULES = {

    "DangerousFunction": {
        "severity": "CRITICAL",
        "score": 90
    },

    "SyntaxError": {
        "severity": "HIGH",
        "score": 85
    },

    "IndentationError": {
        "severity": "HIGH",
        "score": 85
    },

    "DivisionByZero": {
        "severity": "HIGH",
        "score": 80
    },

    "InfiniteLoop": {
        "severity": "HIGH",
        "score": 80
    },

    "UndefinedName": {
        "severity": "MEDIUM",
        "score": 60
    },

    "PossibleTypeError": {
        "severity": "MEDIUM",
        "score": 65
    },

    "BreakOutsideLoop": {
        "severity": "MEDIUM",
        "score": 55
    },

    "ContinueOutsideLoop": {
        "severity": "MEDIUM",
        "score": 55
    },

    "MutableDefaultArgument": {
        "severity": "LOW",
        "score": 35
    },

    "BareExcept": {
        "severity": "LOW",
        "score": 30
    },

    "BuiltinShadowing": {
        "severity": "LOW",
        "score": 25
    },

    "UnusedImport": {
        "severity": "LOW",
        "score": 20
    }
}


def calculate_severity(issue: Issue) -> Issue:

    rule = SEVERITY_RULES.get(
        issue.error_type
    )

    if rule:

        issue.severity = rule["severity"]

        issue.error_score = rule["score"]

    else:

        issue.severity = "MEDIUM"

        issue.error_score = 50

    return issue


def calculate_all_severities(issues):

    updated_issues = []

    for issue in issues:

        updated_issue = calculate_severity(
            issue
        )

        updated_issues.append(
            updated_issue
        )

    return updated_issues