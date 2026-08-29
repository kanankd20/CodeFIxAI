"""
=============================================================
                       CODEFIX AI
                    DATASET LOADER
=============================================================

Purpose:
    Load and validate the CodeFix AI CSV dataset.

Dataset:
    dataset/error_dataset.csv

This module prepares the dataset for future:
    - Feature extraction
    - Machine Learning
    - Error classification
    - Error severity prediction
    - Fix recommendation

=============================================================
"""

from pathlib import Path
import pandas as pd


# ============================================================
# DATASET LOCATION
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_PATH = PROJECT_ROOT / "dataset" / "error_dataset.csv"


# ============================================================
# REQUIRED COLUMNS
# ============================================================

REQUIRED_COLUMNS = [
    "id",
    "language",
    "code",
    "error_type",
    "category",
    "severity",
    "error_score",
    "message",
    "suggestion",
    "fixed_code",
]


# ============================================================
# LOAD DATASET
# ============================================================

def load_dataset():

    """
    Load the CodeFix AI dataset.

    Returns:
        pandas.DataFrame
    """

    if not DATASET_PATH.exists():

        raise FileNotFoundError(
            f"Dataset not found at:\n{DATASET_PATH}"
        )


    try:

        df = pd.read_csv(
            DATASET_PATH,
            encoding="utf-8"
        )

    except Exception as error:

        raise RuntimeError(
            f"Unable to read dataset: {error}"
        )


    return df


# ============================================================
# VALIDATE DATASET
# ============================================================

def validate_dataset(df):

    """
    Validate the structure of the dataset.

    Returns:
        True if dataset is valid.
    """

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]


    if missing_columns:

        raise ValueError(
            "Missing required columns: "
            + ", ".join(missing_columns)
        )


    if df.empty:

        raise ValueError(
            "Dataset is empty."
        )


    return True


# ============================================================
# CLEAN DATASET
# ============================================================

def clean_dataset(df):

    """
    Perform basic dataset cleaning.
    """

    df = df.copy()


    # Remove completely empty rows

    df = df.dropna(
        how="all"
    )


    # Fill text fields

    text_columns = [
        "language",
        "code",
        "error_type",
        "category",
        "severity",
        "message",
        "suggestion",
        "fixed_code",
    ]


    for column in text_columns:

        if column in df.columns:

            df[column] = (
                df[column]
                .fillna("")
                .astype(str)
                .str.strip()
            )


    # Convert error score to numeric

    if "error_score" in df.columns:

        df["error_score"] = pd.to_numeric(
            df["error_score"],
            errors="coerce"
        )

        df["error_score"] = (
            df["error_score"]
            .fillna(0)
            .astype(int)
        )


    return df


# ============================================================
# DATASET SUMMARY
# ============================================================

def dataset_summary(df):

    """
    Generate useful information about the dataset.
    """

    summary = {

        "total_records": len(df),

        "languages": sorted(
            df["language"]
            .dropna()
            .unique()
            .tolist()
        ),

        "error_types": sorted(
            df["error_type"]
            .dropna()
            .unique()
            .tolist()
        ),

        "categories": sorted(
            df["category"]
            .dropna()
            .unique()
            .tolist()
        ),

        "severity_levels": sorted(
            df["severity"]
            .dropna()
            .unique()
            .tolist()
        ),
    }


    return summary


# ============================================================
# COMPLETE DATASET PIPELINE
# ============================================================

def prepare_dataset():

    """
    Complete dataset loading and preparation pipeline.
    """

    df = load_dataset()

    validate_dataset(df)

    df = clean_dataset(df)

    return df


# ============================================================
# TEST / INFORMATION DISPLAY
# ============================================================

if __name__ == "__main__":

    print()

    print("=" * 70)

    print(
        "                    CODEFIX AI"
    )

    print(
        "                    DATASET LOADER"
    )

    print("=" * 70)


    print()

    print(
        "Dataset location:"
    )

    print(
        DATASET_PATH
    )


    # --------------------------------------------------------
    # LOAD
    # --------------------------------------------------------

    try:

        df = prepare_dataset()

    except Exception as error:

        print()

        print(
            "ERROR:"
        )

        print(
            error
        )

        raise SystemExit(1)


    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    summary = dataset_summary(
        df
    )


    print()

    print(
        "DATASET STATUS: READY"
    )

    print()

    print(
        "Total Records :",
        summary["total_records"]
    )

    print(
        "Languages     :",
        ", ".join(summary["languages"])
    )

    print(
        "Error Types   :",
        len(summary["error_types"])
    )

    print(
        "Categories    :",
        len(summary["categories"])
    )

    print(
        "Severity      :",
        ", ".join(summary["severity_levels"])
    )


    # --------------------------------------------------------
    # ERROR TYPES
    # --------------------------------------------------------

    print()

    print(
        "ERROR TYPES"
    )

    print(
        "-" * 50
    )

    for error_type in summary["error_types"]:

        count = (
            df["error_type"] == error_type
        ).sum()

        print(
            f"{error_type:<30} {count}"
        )


    # --------------------------------------------------------
    # SAMPLE
    # --------------------------------------------------------

    print()

    print(
        "SAMPLE RECORD"
    )

    print(
        "-" * 50
    )

    sample = df.iloc[0]

    print(
        "Error Type :",
        sample["error_type"]
    )

    print(
        "Category   :",
        sample["category"]
    )

    print(
        "Severity   :",
        sample["severity"]
    )

    print(
        "Score      :",
        sample["error_score"]
    )


    # --------------------------------------------------------
    # COMPLETE
    # --------------------------------------------------------

    print()

    print("=" * 70)

    print(
        "              DATASET LOADING COMPLETE"
    )

    print("=" * 70)

    print()