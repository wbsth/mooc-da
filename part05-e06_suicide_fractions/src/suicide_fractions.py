#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv('src/who_suicide_statistics.csv')
    df['suicide_ratio'] = df['suicides_no']/df['population']
    final_df = df.groupby('country')
    final_df = final_df['suicide_ratio'].mean()
    return final_df

def main():
    suicide_fractions()

if __name__ == "__main__":
    main()
