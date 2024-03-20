"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.3
"""
import typing as t
import pandas as pd
import logging

from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

logger = logging.getLogger(__name__)

def split_data(df: pd.DataFrame, parameters: t.Dict) -> t.Tuple: 
  X = df[parameters["features"]]
  y = df["price"]
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=parameters["test_size"])
  return X_train, X_test, y_train, y_test

def train_model(
    X_train: pd.DataFrame, 
    y_train: pd.Series) -> LinearRegression:
  regressor = LinearRegression()
  regressor.fit(X_train, y_train)
  return regressor

def evaluate_model(
    regressor: LinearRegression, 
    X_test: pd.DataFrame, 
    y_test: pd.Series,
):
  y_pred = regressor.predict(X_test)
  score = r2_score(y_test, y_pred)
  logger.info("Model has a r^2 of %.3f on test data.", score)

