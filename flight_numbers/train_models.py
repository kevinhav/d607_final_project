import pandas as pd
import numpy as np
import flight_numbers.get_data
from sklearn.linear_model import LinearRegression
import flight_numbers.get_data


def get_x_y(df, x_col, y_col):
    """
    Return X and y arrays for linear regression
    """

    X = df[x_col].values.reshape(-1, 1)
    y = df[y_col].values.reshape(-1, 1)

    return X, y


def build_lm(X, y):

    return LinearRegression().fit(X, y)


def predict_disc_speed(model: LinearRegression, rim_thickness):

    return model.predict(rim_thickness)
