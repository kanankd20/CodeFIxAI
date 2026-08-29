"""
=============================================================
                       CODEFIX AI
                    ML TRAINER - STEP 6.4
=============================================================

Purpose:
    Prepare the ML-ready dataset and create training/testing
    datasets for the CodeFix AI classifier.

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
    ml_dataset.py
            |
            v
    ml_ready_dataset.csv
            |
            v
    ml_trainer.py
            |
       +----+----+
       |         |
       v         v
   Training   Testing
     80%        20%

=============================================================
"""

from pathlib import Path

import pandas as pd

from sklearn.model_selection import train_test_split

from core.ml_dataset import build_ml_dataset


# ============================================================
# PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_DIR = PROJECT_ROOT / "dataset"

TRAIN_PATH = DATASET_DIR / "train_dataset.csv"

TEST_PATH = DATASET_DIR / "test_dataset.csv"


# ============================================================
# TARGET COLUMN
# ============================================================

TARGET_COLUMN = "error_type"


# ============================================================
# FEATURES
# ============================================================

TARGET_COLUMNS = [
    "error_type",
    "category",
    "severity",
    "error_score",
]


# ============================================================
# PREPARE FEATURES
# ============================================================

def prepare_features(df):
    """
    Separate ML features from target information.
    """

    feature_columns = [
        column
        for column in df.columns
        if column not in TARGET_COLUMNS
    ]

    X = df[feature_columns]

    y = df[TARGET_COLUMN]

    return X, y


# ============================================================
# SPLIT DATASET
# ============================================================

def split_dataset(
    df,
    test_size=0.20,
    random_state=42
):
    """
    Split dataset into training and testing data.
    """

    X, y = prepare_features(df)

    # --------------------------------------------------------
    # IMPORTANT
    # --------------------------------------------------------
    # Stratification can fail when an error class contains
    # only one sample. Therefore we check class counts first.
    # --------------------------------------------------------

    class_counts = y.value_counts()

    can_stratify = (
        class_counts.min() >= 2
    )

    stratify_value = y if can_stratify else None

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=stratify_value
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test
    )


# ============================================================
# CREATE TRAINING DATAFRAME
# ============================================================

def create_train_dataframe(
    X_train,
    y_train
):

    train_df = X_train.copy()

    train_df[TARGET_COLUMN] = (
        y_train.values
    )

    return train_df


# ============================================================
# CREATE TEST DATAFRAME
# ============================================================

def create_test_dataframe(
    X_test,
    y_test
):

    test_df = X_test.copy()

    test_df[TARGET_COLUMN] = (
        y_test.values
    )

    return test_df


# ============================================================
# SAVE DATASETS
# ============================================================

def save_datasets(
    train_df,
    test_df
):

    DATASET_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    train_df.to_csv(
        TRAIN_PATH,
        index=False,
        encoding="utf-8"
    )

    test_df.to_csv(
        TEST_PATH,
        index=False,
        encoding="utf-8"
    )


# ============================================================
# DISPLAY INFORMATION
# ============================================================

def display_split_information(
    df,
    train_df,
    test_df
):

    print()

    print("=" * 70)

    print(
        "                    CODEFIX AI"
    )

    print(
        "                 DATASET SPLITTER"
    )

    print("=" * 70)

    print()

    print(
        "ORIGINAL DATASET"
    )

    print(
        "-" * 50
    )

    print(
        "Total records :",
        len(df)
    )

    print()

    print(
        "TRAINING DATA"
    )

    print(
        "-" * 50
    )

    print(
        "Training records :",
        len(train_df)
    )

    print(
        "Training ratio   :",
        f"{len(train_df) / len(df) * 100:.1f}%"
    )

    print()

    print(
        "TESTING DATA"
    )

    print(
        "-" * 50
    )

    print(
        "Testing records  :",
        len(test_df)
    )

    print(
        "Testing ratio    :",
        f"{len(test_df) / len(df) * 100:.1f}%"
    )

    print()

    print(
        "TARGET DISTRIBUTION"
    )

    print(
        "-" * 50
    )

    print(
        df[TARGET_COLUMN]
        .value_counts()
        .to_string()
    )

    print()

    print(
        "FILES CREATED"
    )

    print(
        "-" * 50
    )

    print(
        "Training:",
        TRAIN_PATH
    )

    print(
        "Testing :",
        TEST_PATH
    )

    print()

    print("=" * 70)

    print(
        "              DATASET SPLIT COMPLETE"
    )

    print("=" * 70)

    print()


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    try:

        # ----------------------------------------------------
        # BUILD ML DATASET
        # ----------------------------------------------------

        df = build_ml_dataset()


        # ----------------------------------------------------
        # SPLIT
        # ----------------------------------------------------

        (
            X_train,
            X_test,
            y_train,
            y_test
        ) = split_dataset(
            df
        )


        # ----------------------------------------------------
        # CREATE DATAFRAMES
        # ----------------------------------------------------

        train_df = create_train_dataframe(
            X_train,
            y_train
        )

        test_df = create_test_dataframe(
            X_test,
            y_test
        )


        # ----------------------------------------------------
        # SAVE
        # ----------------------------------------------------

        save_datasets(
            train_df,
            test_df
        )


        # ----------------------------------------------------
        # DISPLAY
        # ----------------------------------------------------

        display_split_information(
            df,
            train_df,
            test_df
        )


    except Exception as error:

        print()

        print("=" * 70)

        print(
            "ERROR WHILE SPLITTING DATASET"
        )

        print("=" * 70)

        print()

        print(
            error
        )

        raise