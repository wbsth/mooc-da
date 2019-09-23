#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep = '\t', index_col=0)
    data = df[1:312]
    cols = data.columns
    filtered = data[(data[cols[2]] > 5) & (data[cols[3]] > 5)]
    print(cols)
    return filtered[[cols[0], cols[2], cols[3]]]

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
