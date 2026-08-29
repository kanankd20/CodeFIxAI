"""
=============================================================
                        CODEFIX AI
                  PYTHON CODE ANALYZER
=============================================================

Main analysis pipeline.

CodeFix AI performs:

    1. Detection
    2. Location
    3. Classification
    4. Severity analysis
    5. Error scoring
    6. Explanation
    7. Fix / Rectification

=============================================================
"""


# ============================================================
# ANALYZERS
# ============================================================

from core.analyzers.syntax_analyzer import analyze_syntax
from core.analyzers.name_analyzer import analyze_names
from core.analyzers.type_analyzer import analyze_types
from core.analyzers.security_analyzer import analyze_security
from core.analyzers.quality_analyzer import analyze_quality
from core.analyzers.control_flow_analyzer import analyze_control_flow


# ============================================================
# PROCESSING MODULES
# ============================================================

from core.classifier import classify_issues
from core.severity import calculate_all_severities
from core.explainer import explain_all_issues
from core.fixer import fix_all_issues


# ============================================================
# MAIN DETECTION FUNCTION
# ============================================================

def detect_errors(code):
    """
    Analyze Python source code.

    Pipeline:

        Detect
        ↓
        Locate
        ↓
        Classify
        ↓
        Severity
        ↓
        Score
        ↓
        Explain
        ↓
        Fix
    """

    # --------------------------------------------------------
    # Master issue list
    # --------------------------------------------------------

    all_issues = []


    # ========================================================
    # STAGE 1 — SYNTAX ANALYSIS
    # ========================================================

    tree, syntax_issues = analyze_syntax(
        code
    )

    all_issues.extend(
        syntax_issues
    )


    # ========================================================
    # IF SYNTAX TREE CANNOT BE CREATED
    # ========================================================

    if tree is None:

        # ----------------------------------------------------
        # Classification
        # ----------------------------------------------------

        classified_issues = classify_issues(
            all_issues
        )


        # ----------------------------------------------------
        # Severity + Score
        # ----------------------------------------------------

        severity_issues = calculate_all_severities(
            classified_issues
        )


        # ----------------------------------------------------
        # Explanation
        # ----------------------------------------------------

        explained_issues = explain_all_issues(
            severity_issues
        )


        # ----------------------------------------------------
        # Fix
        # ----------------------------------------------------

        final_issues = fix_all_issues(
            code,
            explained_issues
        )


        return final_issues


    # ========================================================
    # STAGE 1B — NAME ANALYSIS
    # ========================================================

    name_issues = analyze_names(
        tree
    )

    all_issues.extend(
        name_issues
    )


    # ========================================================
    # STAGE 1C — TYPE ANALYSIS
    # ========================================================

    type_issues = analyze_types(
        tree
    )

    all_issues.extend(
        type_issues
    )


    # ========================================================
    # STAGE 1D — SECURITY ANALYSIS
    # ========================================================

    security_issues = analyze_security(
        tree
    )

    all_issues.extend(
        security_issues
    )


    # ========================================================
    # STAGE 1E — CODE QUALITY ANALYSIS
    # ========================================================

    quality_issues = analyze_quality(
        tree
    )

    all_issues.extend(
        quality_issues
    )


    # ========================================================
    # STAGE 1F — CONTROL FLOW ANALYSIS
    # ========================================================

    control_flow_issues = analyze_control_flow(
        tree
    )

    all_issues.extend(
        control_flow_issues
    )


    # ========================================================
    # STAGE 2 — CLASSIFICATION
    # ========================================================

    classified_issues = classify_issues(
        all_issues
    )


    # ========================================================
    # STAGE 3 — SEVERITY + ERROR SCORE
    # ========================================================

    severity_issues = calculate_all_severities(
        classified_issues
    )


    # ========================================================
    # STAGE 4 — EXPLANATION
    # ========================================================

    explained_issues = explain_all_issues(
        severity_issues
    )


    # ========================================================
    # STAGE 5 — FIX / RECTIFICATION
    # ========================================================

    final_issues = fix_all_issues(
        code,
        explained_issues
    )


    # ========================================================
    # RETURN RESULTS
    # ========================================================

    return final_issues


# ============================================================
# SUMMARY
# ============================================================

def calculate_summary(issues):
    """
    Calculate overall CodeFix AI analysis statistics.
    """

    total = len(
        issues
    )

    critical = 0
    high = 0
    medium = 0
    low = 0

    total_score = 0


    for issue in issues:

        # ----------------------------------------------------
        # Severity
        # ----------------------------------------------------

        severity = str(
            issue.severity
        ).upper()


        if severity == "CRITICAL":

            critical += 1

        elif severity == "HIGH":

            high += 1

        elif severity == "MEDIUM":

            medium += 1

        elif severity == "LOW":

            low += 1


        # ----------------------------------------------------
        # Error score
        # ----------------------------------------------------

        try:

            total_score += float(
                issue.error_score
            )

        except (
            AttributeError,
            TypeError,
            ValueError
        ):

            pass


    # --------------------------------------------------------
    # Average score
    # --------------------------------------------------------

    if total > 0:

        average_score = round(
            total_score / total,
            2
        )

    else:

        average_score = 0


    return {

        "total": total,

        "critical": critical,

        "high": high,

        "medium": medium,

        "low": low,

        "average_score": average_score
    }


# ============================================================
# TERMINAL REPORT
# ============================================================

def print_report(code):
    """
    Run CodeFix AI and display a complete analysis report.
    """

    issues = detect_errors(
        code
    )


    # ========================================================
    # HEADER
    # ========================================================

    print()

    print(
        "=" * 75
    )

    print(
        "                         CODEFIX AI"
    )

    print(
        "                  PYTHON CODE ANALYZER"
    )

    print(
        "=" * 75
    )


    # ========================================================
    # CLEAN CODE
    # ========================================================

    if not issues:

        print()

        print(
            "STATUS           : CLEAN"
        )

        print(
            "TOTAL ISSUES     : 0"
        )

        print(
            "AVERAGE SCORE    : 0/100"
        )

        print()

        print(
            "No detectable issues were found."
        )

        print()

        print(
            "=" * 75
        )

        return


    # ========================================================
    # SUMMARY
    # ========================================================

    summary = calculate_summary(
        issues
    )


    print()

    print(
        f"TOTAL ISSUES     : {summary['total']}"
    )

    print(
        f"CRITICAL ISSUES  : {summary['critical']}"
    )

    print(
        f"HIGH ISSUES      : {summary['high']}"
    )

    print(
        f"MEDIUM ISSUES    : {summary['medium']}"
    )

    print(
        f"LOW ISSUES       : {summary['low']}"
    )

    print(
        f"AVERAGE SCORE    : {summary['average_score']}/100"
    )


    # ========================================================
    # ISSUE DETAILS
    # ========================================================

    print()

    print(
        "=" * 75
    )

    print(
        "                       ISSUE DETAILS"
    )

    print(
        "=" * 75
    )


    for number, issue in enumerate(
        issues,
        start=1
    ):

        print()

        print(
            "-" * 75
        )

        print(
            f"ISSUE #{number}"
        )

        print(
            "-" * 75
        )


        # ----------------------------------------------------
        # BASIC INFORMATION
        # ----------------------------------------------------

        print(
            f"Error Type    : {issue.error_type}"
        )

        print(
            f"Category      : {issue.category}"
        )


        # ----------------------------------------------------
        # LOCATION
        # ----------------------------------------------------

        print(
            f"Line          : {issue.line}"
        )

        print(
            f"Column        : {issue.column}"
        )


        # ----------------------------------------------------
        # MESSAGE
        # ----------------------------------------------------

        print(
            f"Message       : {issue.message}"
        )


        # ----------------------------------------------------
        # SEVERITY
        # ----------------------------------------------------

        print(
            f"Severity      : {issue.severity}"
        )


        # ----------------------------------------------------
        # ERROR SCORE
        # ----------------------------------------------------

        print(
            f"Error Score   : {issue.error_score}/100"
        )


        # ----------------------------------------------------
        # CONFIDENCE
        # ----------------------------------------------------

        print(
            f"Confidence    : {issue.confidence}%"
        )


        # ----------------------------------------------------
        # FIX STATUS
        # ----------------------------------------------------

        fix_type = getattr(
            issue,
            "fix_type",
            "UNKNOWN"
        )


        if fix_type == "AUTOMATIC":

            print(
                "Fix Status    : AUTOMATIC FIX AVAILABLE"
            )

        elif fix_type == "SUGGESTED":

            print(
                "Fix Status    : FIX SUGGESTION AVAILABLE"
            )

        elif fix_type == "MANUAL":

            print(
                "Fix Status    : MANUAL FIX REQUIRED"
            )

        else:

            print(
                "Fix Status    : NOT AVAILABLE"
            )


        # ====================================================
        # EXPLANATION
        # ====================================================

        explanation = getattr(
            issue,
            "explanation",
            None
        )


        if explanation:

            print()

            print(
                "EXPLANATION"
            )

            print(
                "-" * 50
            )

            print(
                explanation
            )


        # ====================================================
        # SUGGESTED SOLUTION
        # ====================================================

        suggestion = getattr(
            issue,
            "suggestion",
            None
        )


        if suggestion:

            print()

            print(
                "SUGGESTED SOLUTION"
            )

            print(
                "-" * 50
            )

            print(
                suggestion
            )


        # ====================================================
        # FIX EXAMPLE
        # ====================================================

        fix_example = getattr(
            issue,
            "fix_example",
            None
        )


        if fix_example:

            print()

            print(
                "FIX EXAMPLE"
            )

            print(
                "-" * 50
            )

            print(
                fix_example
            )


        # ====================================================
        # AUTOMATICALLY FIXED CODE
        # ====================================================

        fixed_code = getattr(
            issue,
            "fixed_code",
            None
        )


        if fixed_code:

            print()

            print(
                "AUTOMATICALLY CORRECTED CODE"
            )

            print(
                "-" * 50
            )

            print(
                fixed_code
            )


    # ========================================================
    # FINAL MESSAGE
    # ========================================================

    print()

    print(
        "=" * 75
    )

    print(
        "              CODEFIX AI ANALYSIS COMPLETE"
    )

    print(
        "=" * 75
    )


# ============================================================
# TEST CODE
# ============================================================

if __name__ == "__main__":

    test_code = """
import math

x = "Hello"
y = 10

print(z)

result = x + y

eval("print('hello')")


def test(items=[]):

    try:
        print(x)

    except:
        pass

    return 10
"""


    print_report(
        test_code
    )