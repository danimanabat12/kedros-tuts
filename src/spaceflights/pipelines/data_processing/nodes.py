"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

import pandas as pd


def _is_true(x: pd.Series) -> pd.Series:
    """Convert t/f values to their corresponding Boolean value (True or False)"""
    return x == "t"


def _parse_percentage(x: pd.Series) -> pd.Series:
    """Convert percentage values to its corresponding numerical representation"""
    return x.str.replace("%", "").astype(float)


def _parse_money(x: pd.Series) -> pd.Series:
    """Convert money to numerical representation"""
    return x.str.replace("$", "").str.replace(",", "").astype(float)


def preprocess_companies(df: pd.DataFrame) -> pd.DataFrame:
    df["iata_approved"] = _is_true(df["iata_approved"])
    df["company_rating"] = _parse_percentage(df["company_rating"])
    return df


def preprocess_shuttles(df: pd.DataFrame) -> pd.DataFrame:
    df["d_check_complete"] = _is_true(df["d_check_complete"])
    df["moon_clearance_complete"] = _is_true(df["moon_clearance_complete"])
    df["price"] = _parse_money(df["price"])
    return df
