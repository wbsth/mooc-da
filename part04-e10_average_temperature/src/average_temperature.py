#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    df_july = df[df.m == 7]
    print(df_july.describe())
    return df_july.describe().iloc[1,-1]

def main():
    print(f"Average temperature in July: {average_temperature()}")

if __name__ == "__main__":
    main()
