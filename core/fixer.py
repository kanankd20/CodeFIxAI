"""
=============================================================
                       CODEFIX AI
                      FIXER ENGINE
=============================================================

Purpose:
    Provides correction suggestions and safe automatic fixes
    for detected Python programming issues.

Pipeline:

    Detection
        ↓
    Classification
        ↓
    Severity + Score
        ↓
    Explanation
        ↓
    Fix / Rectification

IMPORTANT:
    CodeFix AI never executes user-submitted code.

=============================================================
"""


# ============================================================
# FIX RULE DATABASE
# ============================================================

FIX_RULES = {

    # --------------------------------------------------------
    # Undefined Name
    # --------------------------------------------------------

    "UndefinedName": {

        "fix_type": "MANUAL",

        "description": (
            "Define the variable, function, or name before "
            "using it."
        ),

        "example": (
            "Check the spelling of the name and define it "
            "before the line where it is used."
        )
    },


    # --------------------------------------------------------
    # Dangerous Function
    # --------------------------------------------------------

    "DangerousFunction": {

        "fix_type": "MANUAL",

        "description": (
            "Avoid eval() or exec() when processing untrusted "
            "input."
        ),

        "example": (
            "Use a specific parser such as int(), float(), "
            "json.loads(), or another safe alternative."
        )
    },


    # --------------------------------------------------------
    # Mutable Default Argument
    # --------------------------------------------------------

    "MutableDefaultArgument": {

        "fix_type": "SUGGESTED",

        "description": (
            "Use None as the default value and create the "
            "mutable object inside the function."
        ),

        "example": (
            "def function(items=None):\n"
            "    if items is None:\n"
            "        items = []"
        )
    },


    # --------------------------------------------------------
    # Bare Except
    # --------------------------------------------------------

    "BareExcept": {

        "fix_type": "AUTOMATIC",

        "description": (
            "Replace the bare except statement with a more "
            "specific exception type."
        ),

        "example": (
            "except Exception:"
        )
    },


    # --------------------------------------------------------
    # Built-in Shadowing
    # --------------------------------------------------------

    "BuiltinShadowing": {

        "fix_type": "MANUAL",

        "description": (
            "Rename the variable so that it does not use "
            "the name of a Python built-in."
        ),

        "example": (
            "Instead of 'list', use a name such as "
            "'numbers' or 'items'."
        )
    },


    # --------------------------------------------------------
    # Possible Type Error
    # --------------------------------------------------------

    "PossibleTypeError": {

        "fix_type": "MANUAL",

        "description": (
            "Convert values to compatible data types before "
            "performing the operation."
        ),

        "example": (
            "Use str(), int(), float(), or another appropriate "
            "conversion."
        )
    },


    # --------------------------------------------------------
    # Division By Zero
    # --------------------------------------------------------

    "DivisionByZero": {

        "fix_type": "MANUAL",

        "description": (
            "Check whether the divisor is zero before "
            "performing the division."
        ),

        "example": (
            "if divisor != 0:\n"
            "    result = value / divisor"
        )
    },


    # --------------------------------------------------------
    # Break Outside Loop
    # --------------------------------------------------------

    "BreakOutsideLoop": {

        "fix_type": "MANUAL",

        "description": (
            "Move the break statement inside the appropriate "
            "for or while loop."
        ),

        "example": (
            "Place break inside a for or while loop."
        )
    },


    # --------------------------------------------------------
    # Continue Outside Loop
    # --------------------------------------------------------

    "ContinueOutsideLoop": {

        "fix_type": "MANUAL",

        "description": (
            "Move the continue statement inside the appropriate "
            "for or while loop."
        ),

        "example": (
            "Place continue inside a for or while loop."
        )
    },


    # --------------------------------------------------------
    # Infinite Loop
    # --------------------------------------------------------

    "InfiniteLoop": {

        "fix_type": "MANUAL",

        "description": (
            "Make sure the loop condition can eventually "
            "become false."
        ),

        "example": (
            "Update the loop-control variable inside the loop."
        )
    },


    # --------------------------------------------------------
    # Unused Import
    # --------------------------------------------------------

    "UnusedImport": {

        "fix_type": "MANUAL",

        "description": (
            "Remove imports that are not required by the "
            "program."
        ),

        "example": (
            "Delete the unused import statement."
        )
    },


    # --------------------------------------------------------
    # Syntax Error
    # --------------------------------------------------------

    "SyntaxError": {

        "fix_type": "MANUAL",

        "description": (
            "Check the reported line and nearby lines for "
            "missing brackets, colons, quotes, commas, or "
            "other syntax problems."
        ),

        "example": (
            "if x > 10:\n"
            "    print(x)"
        )
    },


    # --------------------------------------------------------
    # Indentation Error
    # --------------------------------------------------------

    "IndentationError": {

        "fix_type": "MANUAL",

        "description": (
            "Correct the indentation and use consistent "
            "spaces throughout the code."
        ),

        "example": (
            "Use four spaces for each indentation level."
        )
    }
}


# ============================================================
# GET FIX RULE
# ============================================================

def get_fix_rule(error_type):
    """
    Return the fix rule for a specific error type.

    Parameters
    ----------
    error_type : str
        Name of the detected error.

    Returns
    -------
    dict or None
        Corresponding fix rule.
    """

    return FIX_RULES.get(
        error_type
    )


# ============================================================
# GET FIX TYPE
# ============================================================

def get_fix_type(error_type):
    """
    Return the type of fix available.

    Possible values:

        AUTOMATIC
        SUGGESTED
        MANUAL
        UNKNOWN
    """

    rule = get_fix_rule(
        error_type
    )

    if rule is None:

        return "UNKNOWN"

    return rule["fix_type"]


# ============================================================
# CREATE FIX SUGGESTION
# ============================================================

def create_fix_suggestion(issue):
    """
    Generate a beginner-friendly fix suggestion.
    """

    rule = get_fix_rule(
        issue.error_type
    )

    if rule is None:

        return (
            "CodeFix AI does not currently have a specific "
            "fix rule for this error."
        )

    return rule["description"]


# ============================================================
# CREATE FIX EXAMPLE
# ============================================================

def create_fix_example(issue):
    """
    Generate a simple example showing how the error
    can be corrected.
    """

    rule = get_fix_rule(
        issue.error_type
    )

    if rule is None:

        return None

    return rule["example"]


# ============================================================
# SAFE AUTOMATIC FIX
# ============================================================

def apply_safe_fix(code, issue):
    """
    Apply only fixes that are considered safe enough for
    simple text transformation.

    Currently:
        BareExcept → except Exception:

    All other issues return the original code.

    This prevents CodeFix AI from making unsafe guesses.
    """

    error_type = issue.error_type


    # --------------------------------------------------------
    # BARE EXCEPT
    # --------------------------------------------------------

    if error_type == "BareExcept":

        corrected_code = code.replace(
            "except:",
            "except Exception:"
        )

        return corrected_code


    # --------------------------------------------------------
    # NO AUTOMATIC FIX
    # --------------------------------------------------------

    return code


# ============================================================
# PROCESS ONE ISSUE
# ============================================================

def fix_issue(code, issue):
    """
    Process one detected issue.

    Adds:

        suggestion
        fix_example
        fix_type
        fixed_code

    to the Issue object.
    """

    # --------------------------------------------------------
    # Suggestion
    # --------------------------------------------------------

    issue.suggestion = create_fix_suggestion(
        issue
    )


    # --------------------------------------------------------
    # Fix example
    # --------------------------------------------------------

    issue.fix_example = create_fix_example(
        issue
    )


    # --------------------------------------------------------
    # Fix type
    # --------------------------------------------------------

    issue.fix_type = get_fix_type(
        issue.error_type
    )


    # --------------------------------------------------------
    # Try safe automatic fix
    # --------------------------------------------------------

    corrected_code = apply_safe_fix(
        code,
        issue
    )


    # --------------------------------------------------------
    # Store corrected code
    # --------------------------------------------------------

    if corrected_code != code:

        issue.fixed_code = corrected_code

    else:

        issue.fixed_code = None


    return issue


# ============================================================
# PROCESS ALL ISSUES
# ============================================================

def fix_all_issues(code, issues):
    """
    Process all detected issues.

    Parameters
    ----------
    code : str
        Original Python source code.

    issues : list
        List of detected Issue objects.

    Returns
    -------
    list
        Updated Issue objects.
    """

    fixed_issues = []


    for issue in issues:

        updated_issue = fix_issue(
            code,
            issue
        )

        fixed_issues.append(
            updated_issue
        )


    return fixed_issues