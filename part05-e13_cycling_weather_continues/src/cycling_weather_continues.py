#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def split_date_continues():
    # reading data from csv
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=";")

    # dropping unecessary rows and columns
    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")

    # extracting first column to separate var
    col = df.iloc[:, 0]
    df = df.drop(df.columns[0], axis=1)

    # splitting data, translating
    col = col.str.split(expand=True)
    col.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    col['Hour'] = col['Hour'].str[0:2]

    weekdays = {
        "ma": "Mon",
        "ti": "Tue",
        "ke": "Wed",
        "to": "Thu",
        "pe": "Fri",
        "la": "Sat",
        "su": "Sun"
    }

    months = {
        "tammi": 1,
        "helmi": 2,
        "maalis": 3,
        "huhti": 4,
        "touko": 5,
        "kesä": 6,
        "heinä": 7,
        "elo": 8,
        "syys": 9,
        "loka": 10,
        "marras": 11,
        "joulu": 12,
    }

    col["Weekday"] = col["Weekday"].map(weekdays)
    col["Month"] = col["Month"].map(months)
    col = col.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

    res = pd.concat([col, df], axis=1)

    return res


def cycling_weather_continues(station):
    df = split_date_continues()
    new_df = pd.merge(df.loc[:, 'Weekday':'Hour'], df.loc[:, station], left_index=True, right_index=True)
    new_df = new_df[new_df.Year == 2017]
    a = new_df.groupby(['Month', 'Day'])[station].sum()
    weather_df = pd.read_csv('src/kumpula-weather-2017.csv')
    final_df = pd.merge(weather_df, a, right_on=['Day', 'Month'], left_on=['d', 'm'])
    final_df = final_df.fillna(method='ffill')
    model = LinearRegression(fit_intercept=True)
    x = final_df.loc[:, ['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    y = final_df.loc[:, station]
    model.fit(x, y)
    score = model.score(x, y)

    return model.coef_, score

def main():
    station = 'Baana'
    coef, score = cycling_weather_continues(station)
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {score:.2f}")




if __name__ == "__main__":
    main()
