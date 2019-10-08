#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    # loading the data, tab as separator
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')

    # different dataframes for X's and Y's columns
    x = df.loc[:, 'X1':'X5']
    y = df.loc[:, 'Y']

    # creating linear regression model
    model = linear_model.LinearRegression(fit_intercept=True)

    # training model using data
    model.fit(x, y)
    score = model.score(x, y)

    rtr = [score]

    for i in range(len(x.columns)):
        a = x.iloc[:, i].values.reshape(-1, 1)
        model.fit(a, y)
        rtr.append(model.score(a, y))

    return rtr


def main():
    x = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {x[0]}")
    for i in range(1, len(x)):
        print(f"R2-score with feature(s) X{i}: {x[i]}")


if __name__ == "__main__":
    main()
