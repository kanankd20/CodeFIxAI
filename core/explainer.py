"""
=============================================================
                 CODEFIX AI EXPLAINER
=============================================================

Converts technical error detections into beginner-friendly
explanations.

=============================================================
"""

from core.error_knowledge import get_error_knowledge


def explain_issue(issue):

    """
    Add explanation information to one Issue object.
    """

    knowledge = get_error_knowledge(
        issue.error_type
    )

    # ---------------------------------------------------------
    # Unknown error
    # ---------------------------------------------------------

    if knowledge is None:

        issue.explanation = (
            "CodeFix AI detected this issue, but a detailed "
            "explanation is not currently available."
        )

        issue.suggestion = (
            "Review the reported line and inspect the surrounding "
            "code for the cause of the problem."
        )

        return issue


    # ---------------------------------------------------------
    # Build beginner-friendly explanation
    # ---------------------------------------------------------

    issue.explanation = (

        f"What is it?\n"
        f"{knowledge['description']}\n\n"

        f"Why did it happen?\n"
        f"{knowledge['cause']}\n\n"

        f"What is the impact?\n"
        f"{knowledge['impact']}"
    )


    # ---------------------------------------------------------
    # Suggestion
    # ---------------------------------------------------------

    issue.suggestion = (
        knowledge["solution"]
    )


    return issue


def explain_all_issues(issues):

    """
    Explain every detected issue.
    """

    explained_issues = []

    for issue in issues:

        explained_issue = explain_issue(
            issue
        )

        explained_issues.append(
            explained_issue
        )

    return explained_issues