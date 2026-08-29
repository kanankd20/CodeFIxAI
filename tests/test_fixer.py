"""
=============================================================
                  CODEFIX AI
               COMPLETE FIXER TEST
=============================================================

Tests multiple CodeFix AI capabilities:

    - Error Detection
    - Error Location
    - Classification
    - Severity
    - Error Score
    - Confidence
    - Explanation
    - Fix Suggestion
    - Automatic Fix

=============================================================
"""

import sys
from pathlib import Path


# ============================================================
# PROJECT ROOT
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:

    sys.path.insert(
        0,
        str(PROJECT_ROOT)
    )


# ============================================================
# CODEFIX AI
# ============================================================

from core.detector import detect_errors


# ============================================================
# TEST PROGRAM
# ============================================================

test_code = """
import math

x = 10

print(z)

result = x + "hello"

eval("print('dangerous')")


def add_items(items=[]):

    items.append(10)

    return items


try:

    print(x)

except:

    pass
"""


# ============================================================
# HEADER
# ============================================================

print()

print("=" * 75)

print(
    "                         CODEFIX AI"
)

print(
    "                    COMPLETE FIXER TEST"
)

print("=" * 75)


# ============================================================
# DISPLAY INPUT
# ============================================================

print()

print(
    "TEST SOURCE CODE"
)

print("-" * 75)

print(
    test_code
)

print("-" * 75)


# ============================================================
# RUN ANALYSIS
# ============================================================

print()

print(
    "Analyzing source code..."
)

issues = detect_errors(
    test_code
)


# ============================================================
# NO ISSUES
# ============================================================

if not issues:

    print()

    print(
        "STATUS: CLEAN"
    )

    print(
        "No detectable issues were found."
    )


# ============================================================
# ISSUES FOUND
# ============================================================

else:

    print()

    print(
        f"TOTAL ISSUES DETECTED: {len(issues)}"
    )


    # ========================================================
    # ISSUE LOOP
    # ========================================================

    for number, issue in enumerate(
        issues,
        start=1
    ):

        print()

        print("=" * 75)

        print(
            f"ISSUE #{number}"
        )

        print("=" * 75)


        # ----------------------------------------------------
        # BASIC INFORMATION
        # ----------------------------------------------------

        print(
            "Error Type       :",
            issue.error_type
        )

        print(
            "Category         :",
            issue.category
        )

        print(
            "Line             :",
            issue.line
        )

        print(
            "Column           :",
            issue.column
        )

        print(
            "Message          :",
            issue.message
        )


        # ----------------------------------------------------
        # SEVERITY
        # ----------------------------------------------------

        print()

        print(
            "Severity         :",
            issue.severity
        )

        print(
            "Error Score      :",
            issue.error_score,
            "/100"
        )

        print(
            "Confidence       :",
            issue.confidence,
            "%"
        )


        # ----------------------------------------------------
        # EXPLANATION
        # ----------------------------------------------------

        print()

        print(
            "EXPLANATION"
        )

        print(
            "-" * 60
        )

        print(
            getattr(
                issue,
                "explanation",
                "No explanation available."
            )
        )


        # ----------------------------------------------------
        # FIX TYPE
        # ----------------------------------------------------

        print()

        print(
            "FIX TYPE"
        )

        print(
            "-" * 60
        )

        print(
            getattr(
                issue,
                "fix_type",
                "UNKNOWN"
            )
        )


        # ----------------------------------------------------
        # SUGGESTION
        # ----------------------------------------------------

        print()

        print(
            "SUGGESTED SOLUTION"
        )

        print(
            "-" * 60
        )

        print(
            getattr(
                issue,
                "suggestion",
                "No suggestion available."
            )
        )


        # ----------------------------------------------------
        # FIX EXAMPLE
        # ----------------------------------------------------

        print()

        print(
            "FIX EXAMPLE"
        )

        print(
            "-" * 60
        )

        print(
            getattr(
                issue,
                "fix_example",
                "No fix example available."
            )
        )


        # ----------------------------------------------------
        # AUTOMATIC FIX
        # ----------------------------------------------------

        fixed_code = getattr(
            issue,
            "fixed_code",
            None
        )


        print()

        print(
            "AUTOMATIC FIX"
        )

        print(
            "-" * 60
        )


        if fixed_code:

            print(
                "AVAILABLE"
            )

            print()

            print(
                fixed_code
            )

        else:

            print(
                "Not available for this issue."
            )


# ============================================================
# COMPLETE
# ============================================================

print()

print("=" * 75)

print(
    "                 CODEFIX AI TEST COMPLETE"
)

print("=" * 75)

print()