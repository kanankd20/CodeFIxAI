"""
=============================================================
                 CODEFIX AI ERROR KNOWLEDGE
=============================================================

Contains beginner-friendly information about common
programming errors detected by CodeFix AI.

This file is the knowledge base for the explanation engine.

=============================================================
"""


ERROR_KNOWLEDGE = {

    # =========================================================
    # 1. UNDEFINED NAME
    # =========================================================

    "UndefinedName": {

        "title": "Undefined Variable or Name",

        "description": (
            "The program is trying to use a variable, function, "
            "or name that has not been defined in the current "
            "scope."
        ),

        "cause": (
            "This usually happens because the variable was "
            "misspelled, forgotten, defined later, or is outside "
            "the current scope."
        ),

        "impact": (
            "Python cannot determine what the name refers to, "
            "so the program will fail when that statement is "
            "executed."
        ),

        "solution": (
            "Make sure the name is defined before it is used "
            "and check the spelling carefully."
        ),

        "example_bad": """print(username)""",

        "example_good": """username = "Kanan"
print(username)"""
    },


    # =========================================================
    # 2. SYNTAX ERROR
    # =========================================================

    "SyntaxError": {

        "title": "Syntax Error",

        "description": (
            "The Python code does not follow the grammatical "
            "rules required by the Python language."
        ),

        "cause": (
            "Common causes include missing colons, brackets, "
            "quotes, commas, operators, or incorrect indentation."
        ),

        "impact": (
            "Python cannot parse the program, so the code cannot "
            "start executing."
        ),

        "solution": (
            "Check the reported line and the line immediately "
            "before it for missing or incorrectly placed syntax."
        ),

        "example_bad": """if x > 10
    print(x)""",

        "example_good": """if x > 10:
    print(x)"""
    },


    # =========================================================
    # 3. INDENTATION ERROR
    # =========================================================

    "IndentationError": {

        "title": "Indentation Error",

        "description": (
            "Python uses indentation to define blocks of code. "
            "The indentation in this code is inconsistent or "
            "incorrect."
        ),

        "cause": (
            "This can happen when spaces and tabs are mixed or "
            "when a statement is not aligned with the block "
            "structure."
        ),

        "impact": (
            "Python cannot correctly determine the structure "
            "of the program."
        ),

        "solution": (
            "Use consistent indentation, normally four spaces "
            "per indentation level."
        ),

        "example_bad": """if x > 5:
print(x)""",

        "example_good": """if x > 5:
    print(x)"""
    },


    # =========================================================
    # 4. POSSIBLE TYPE ERROR
    # =========================================================

    "PossibleTypeError": {

        "title": "Possible Type Error",

        "description": (
            "The program appears to be performing an operation "
            "between values whose data types may not be "
            "compatible."
        ),

        "cause": (
            "Different Python data types support different "
            "operations. For example, a string and an integer "
            "cannot normally be added directly."
        ),

        "impact": (
            "The program may raise a TypeError when this "
            "operation is executed."
        ),

        "solution": (
            "Convert the values to compatible types before "
            "performing the operation."
        ),

        "example_bad": """name = "Kanan"
age = 21

result = name + age""",

        "example_good": """name = "Kanan"
age = 21

result = name + str(age)"""
    },


    # =========================================================
    # 5. DANGEROUS FUNCTION
    # =========================================================

    "DangerousFunction": {

        "title": "Potentially Dangerous Function",

        "description": (
            "The code uses a function such as eval() or exec() "
            "that can dynamically execute Python code."
        ),

        "cause": (
            "Functions such as eval() and exec() are sometimes "
            "used for dynamic programming but can become unsafe "
            "when they process untrusted input."
        ),

        "impact": (
            "If untrusted input reaches these functions, an "
            "attacker may potentially execute unintended code."
        ),

        "solution": (
            "Avoid eval() or exec() when possible. Use safer "
            "alternatives designed for the specific task."
        ),

        "example_bad": """user_input = input("Enter code: ")
eval(user_input)""",

        "example_good": """user_input = input("Enter a number: ")
number = int(user_input)

print(number)"""
    },


    # =========================================================
    # 6. MUTABLE DEFAULT ARGUMENT
    # =========================================================

    "MutableDefaultArgument": {

        "title": "Mutable Default Function Argument",

        "description": (
            "A mutable object such as a list, dictionary, or "
            "set is being used as a function's default argument."
        ),

        "cause": (
            "Python creates the default argument once when the "
            "function is defined rather than creating a new "
            "mutable object on every function call."
        ),

        "impact": (
            "Data can unexpectedly persist between function "
            "calls and produce difficult-to-find bugs."
        ),

        "solution": (
            "Use None as the default value and create the mutable "
            "object inside the function."
        ),

        "example_bad": """def add_item(item, items=[]):
    items.append(item)
    return items""",

        "example_good": """def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items"""
    },


    # =========================================================
    # 7. BARE EXCEPT
    # =========================================================

    "BareExcept": {

        "title": "Bare Except Statement",

        "description": (
            "The code catches all exceptions without specifying "
            "which type of exception should be handled."
        ),

        "cause": (
            "The programmer may have used except: as a quick "
            "way to prevent the program from stopping."
        ),

        "impact": (
            "Unexpected errors can be hidden, making debugging "
            "and maintenance more difficult."
        ),

        "solution": (
            "Catch the specific exception types that the program "
            "is expected to handle."
        ),

        "example_bad": """try:
    result = 10 / x
except:
    pass""",

        "example_good": """try:
    result = 10 / x
except ZeroDivisionError:
    result = 0"""
    },


    # =========================================================
    # 8. BUILTIN SHADOWING
    # =========================================================

    "BuiltinShadowing": {

        "title": "Python Built-in Name Shadowing",

        "description": (
            "A variable or function has been given the same name "
            "as a Python built-in function or object."
        ),

        "cause": (
            "Names such as list, str, sum, input, or id may be "
            "used as ordinary variable names."
        ),

        "impact": (
            "The original Python built-in may become inaccessible "
            "within that scope."
        ),

        "solution": (
            "Rename the variable so that it does not conflict "
            "with a Python built-in."
        ),

        "example_bad": """list = [1, 2, 3]""",

        "example_good": """numbers = [1, 2, 3]"""
    },


    # =========================================================
    # 9. BREAK OUTSIDE LOOP
    # =========================================================

    "BreakOutsideLoop": {

        "title": "Break Used Outside a Loop",

        "description": (
            "The break statement is being used outside a for "
            "or while loop."
        ),

        "cause": (
            "The break statement may have been placed in the "
            "wrong block or indentation level."
        ),

        "impact": (
            "Python cannot use break to terminate a loop that "
            "does not exist at that location."
        ),

        "solution": (
            "Move the break statement inside the appropriate "
            "for or while loop."
        ),

        "example_bad": """if x > 10:
    break""",

        "example_good": """while x > 0:
    if x > 10:
        break

    x -= 1"""
    },


    # =========================================================
    # 10. CONTINUE OUTSIDE LOOP
    # =========================================================

    "ContinueOutsideLoop": {

        "title": "Continue Used Outside a Loop",

        "description": (
            "The continue statement is being used outside a "
            "for or while loop."
        ),

        "cause": (
            "The continue statement may have been placed outside "
            "the loop because of incorrect code structure."
        ),

        "impact": (
            "Python cannot continue to the next iteration when "
            "there is no active loop."
        ),

        "solution": (
            "Move continue inside the appropriate loop."
        ),

        "example_bad": """if x > 10:
    continue""",

        "example_good": """for number in numbers:

    if number < 0:
        continue

    print(number)"""
    },


    # =========================================================
    # 11. DIVISION BY ZERO
    # =========================================================

    "DivisionByZero": {

        "title": "Division by Zero",

        "description": (
            "The program attempts to divide a value by zero."
        ),

        "cause": (
            "The divisor may have been directly set to zero or "
            "may have received a zero value during execution."
        ),

        "impact": (
            "Python can raise a ZeroDivisionError and stop the "
            "affected operation."
        ),

        "solution": (
            "Check the divisor before performing the division "
            "or handle ZeroDivisionError appropriately."
        ),

        "example_bad": """result = 10 / 0""",

        "example_good": """divisor = 0

if divisor != 0:
    result = 10 / divisor
else:
    result = 0"""
    },


    # =========================================================
    # 12. INFINITE LOOP
    # =========================================================

    "InfiniteLoop": {

        "title": "Potential Infinite Loop",

        "description": (
            "The program may contain a loop whose termination "
            "condition is never reached."
        ),

        "cause": (
            "The loop condition may never become false or the "
            "loop-control variable may never be updated."
        ),

        "impact": (
            "The program can continue running indefinitely and "
            "consume CPU resources."
        ),

        "solution": (
            "Ensure that the loop has a reachable termination "
            "condition and that relevant variables are updated."
        ),

        "example_bad": """x = 1

while x > 0:
    print(x)""",

        "example_good": """x = 1

while x > 0:
    print(x)
    x -= 1"""
    },


    # =========================================================
    # 13. UNUSED IMPORT
    # =========================================================

    "UnusedImport": {

        "title": "Unused Import",

        "description": (
            "A module or object has been imported but does not "
            "appear to be used in the analyzed code."
        ),

        "cause": (
            "The import may have been left behind after code "
            "was modified or may have been added unnecessarily."
        ),

        "impact": (
            "Unused imports can make code less clean and may "
            "increase unnecessary dependencies."
        ),

        "solution": (
            "Remove imports that are not required by the program."
        ),

        "example_bad": """import math

print("Hello")""",

        "example_good": """import math

print(math.sqrt(25))"""
    }
}


# ============================================================
# HELPER FUNCTION
# ============================================================

def get_error_knowledge(error_type):

    """
    Return the knowledge entry for an error type.

    If the error is not present in the knowledge base,
    return None.
    """

    return ERROR_KNOWLEDGE.get(
        error_type
    )