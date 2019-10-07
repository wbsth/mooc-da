#!/usr/bin/env python3

import pandas as pd


def suicide_fractions():
    df = pd.read_csv('src/who_suicide_statistics.csv')
    df['suicide_ratio'] = df['suicides_no'] / df['population']
    final_df = df.groupby('country')
    final_df = final_df['suicide_ratio'].mean()
    return final_df


def suicide_weather():
    weather_df = pd.read_html('src/file.html')
    weather_df = weather_df[0]
    weather_df = weather_df.set_index(weather_df.columns[0])
    weather_df = weather_df.iloc[:, 0].str.replace("\u2212", "-").astype(float)
    suicide_fractions_df = suicide_fractions()
    new_df = pd.merge(weather_df, suicide_fractions_df, left_index=True, right_index=True)
    correlation = new_df.corr(method='spearman').iloc[0, 1]
    (suicide_rows, temperature_rows, common_rows) = (x.shape[0] for x in [suicide_fractions_df, weather_df, new_df])

    return suicide_rows, temperature_rows, common_rows, correlation


def main():
    suicide_rows, temperature_rows, common_rows, correlation = suicide_weather()
    print(f"Suicide DataFrame has {suicide_rows} rows")
    print(f"Temperature DataFrame has {temperature_rows} rows")
    print(f"Common DataFrame has {common_rows} rows")
    print(f"Spearman correlation: {correlation}")
    return


if __name__ == "__main__":
    main()
