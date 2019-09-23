#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    df = pd.read_csv("src/municipal.tsv", sep = '\t', index_col=0)
    col = df.columns
    return df.loc['Akaa':'Äänekoski'][[col[0], col[2], col[3]]]

def main():
    print(subsetting_with_loc(df))

if __name__ == "__main__":
    main()
