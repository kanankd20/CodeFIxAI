"""
=============================================================
                       CODEFIX AI
                    ML DATASET BUILDER
=============================================================

Purpose:
    Convert the CodeFix AI CSV dataset into a machine-learning
    ready dataset.

Pipeline:

    error_dataset.csv
            |
            v
    dataset_loader.py
            |
            v
    feature_extractor.py
            |
            v
    ML Dataset
            |
            v
    Machine Learning Model

=============================================================
"""

from pathlib import Path

import pandas as pd

from core.dataset_loader import prepare_dataset
from core.feature_extractor import extract_dataset_features


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_DIR = PROJECT_ROOT / "dataset"

ML_DATASET_PATH = (
    DATASET_DIR / "ml_ready_dataset.csv"
)


# ============================================================
# TARGET COLUMNS
# ============================================================

TARGET_COLUMNS = [
    "error_type",
    "category",
    "severity",
    "error_score",
]


# ============================================================
# BUILD ML DATASET
# ============================================================

def build_ml_dataset():

    """
    Load the original dataset and convert source code into
    numerical features.

    Returns:
        pandas.DataFrame
    """

    # --------------------------------------------------------
    # LOAD ORIGINAL DATASET
    # --------------------------------------------------------

    df = prepare_dataset()


    # --------------------------------------------------------
    # EXTRACT CODE FEATURES
    # --------------------------------------------------------

    features = extract_dataset_features(
        df
    )


    # --------------------------------------------------------
    # ADD TARGET LABELS
    # --------------------------------------------------------

    ml_df = features.copy()


    ml_df["error_type"] = (
        df["error_type"]
        .values
    )


    ml_df["category"] = (
        df["category"]
        .values
    )


    ml_df["severity"] = (
        df["severity"]
        .values
    )


    ml_df["error_score"] = (
        df["error_score"]
        .values
    )


    return ml_df


# ============================================================
# SAVE ML DATASET
# ============================================================

def save_ml_dataset(
    ml_df
):

    """
    Save the ML-ready dataset.
    """

    DATASET_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    ml_df.to_csv(
        ML_DATASET_PATH,
        index=False,
        encoding="utf-8"
    )


    return ML_DATASET_PATH


# ============================================================
# DISPLAY INFORMATION
# ============================================================

def display_dataset_info(
    ml_df
):

    print()

    print("=" * 75)

    print(
        "                    CODEFIX AI"
    )

    print(
        "                 ML DATASET BUILDER"
    )

    print("=" * 75)


    # --------------------------------------------------------
    # BASIC INFORMATION
    # --------------------------------------------------------

    print()

    print(
        "ML DATASET STATUS: READY"
    )

    print()

    print(
        "Total Records :",
        len(ml_df)
    )

    print(
        "Total Features:",
        len(ml_df.columns)
    )


    # --------------------------------------------------------
    # FEATURE LIST
    # --------------------------------------------------------

    print()

    print(
        "FEATURES"
    )

    print(
        "-" * 55
    )


    feature_columns = [
        column
        for column in ml_df.columns
        if column not in TARGET_COLUMNS
    ]


    for number, column in enumerate(
        feature_columns,
        start=1
    ):

        print(
            f"{number:>2}. {column}"
        )


    # --------------------------------------------------------
    # TARGET LABELS
    # --------------------------------------------------------

    print()

    print(
        "TARGET LABELS"
    )

    print(
        "-" * 55
    )


    for column in TARGET_COLUMNS:

        unique_values = (
            ml_df[column]
            .dropna()
            .unique()
        )


        print()

        print(
            f"{column}:"
        )

        print(
            ", ".join(
                str(value)
                for value in unique_values
            )
        )


    # --------------------------------------------------------
    # ERROR DISTRIBUTION
    # --------------------------------------------------------

    print()

    print(
        "ERROR TYPE DISTRIBUTION"
    )

    print(
        "-" * 55
    )


    counts = (
        ml_df["error_type"]
        .value_counts()
    )


    for error_type, count in counts.items():

        print(
            f"{error_type:<35} {count}"
        )


    # --------------------------------------------------------
    # SAMPLE
    # --------------------------------------------------------

    print()

    print(
        "FIRST ML RECORD"
    )

    print(
        "-" * 55
    )


    first_row = ml_df.iloc[0]


    for column in ml_df.columns:

        print(
            f"{column:<30} : {first_row[column]}"
        )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    try:

        # ----------------------------------------------------
        # BUILD
        # ----------------------------------------------------

        ml_df = build_ml_dataset()


        # ----------------------------------------------------
        # SAVE
        # ----------------------------------------------------

        output_path = save_ml_dataset(
            ml_df
        )


        # ----------------------------------------------------
        # DISPLAY
        # ----------------------------------------------------

        display_dataset_info(
            ml_df
        )


        # ----------------------------------------------------
        # OUTPUT FILE
        # ----------------------------------------------------

        print()

        print(
            "ML Dataset saved at:"
        )

        print(
            output_path
        )


        # ----------------------------------------------------
        # COMPLETE
        # ----------------------------------------------------

        print()

        print("=" * 75)

        print(
            "              ML DATASET BUILD COMPLETE"
        )

        print("=" * 75)

        print()


    except Exception as error:

        print()

        print("=" * 75)

        print(
            "ERROR WHILE BUILDING ML DATASET"
        )

        print("=" * 75)

        print()

        print(
            error
        )

        print()

        raise