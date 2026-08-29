"""
=============================================================
                       CODEFIX AI
                         MODELS
=============================================================

Defines the data structures used by CodeFix AI.

The Issue class represents one detected programming problem.

=============================================================
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Issue:

    # ========================================================
    # BASIC ERROR INFORMATION
    # ========================================================

    error_type: str

    category: str

    line: Optional[int]

    column: Optional[int]

    message: str


    # ========================================================
    # ANALYSIS INFORMATION
    # ========================================================

    severity: str = "MEDIUM"

    confidence: float = 0.0

    error_score: int = 0


    # ========================================================
    # EXPLANATION
    # ========================================================

    explanation: str = ""

    suggestion: str = ""


    # ========================================================
    # FIX INFORMATION
    # ========================================================

    fix_type: str = "UNKNOWN"

    fix_example: Optional[str] = None

    fixed_code: Optional[str] = None


    # ========================================================
    # CONVERT ISSUE TO DICTIONARY
    # ========================================================

    def to_dict(self):

        return {

            "error_type": self.error_type,

            "category": self.category,

            "line": self.line,

            "column": self.column,

            "message": self.message,

            "severity": self.severity,

            "confidence": self.confidence,

            "error_score": self.error_score,

            "explanation": self.explanation,

            "suggestion": self.suggestion,

            "fix_type": self.fix_type,

            "fix_example": self.fix_example,

            "fixed_code": self.fixed_code
        }