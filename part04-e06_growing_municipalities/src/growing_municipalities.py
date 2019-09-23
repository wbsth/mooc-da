#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    all = df.shape[0]
    col = df.columns
    filtered = df[df[col[1]] > 0].index
    part = (len(filtered) / all) 
    return(part)

def main():
    df = pd.read_csv("src/municipal.tsv", sep = '\t', index_col=0)
    data = df[1:312]
    percentage = growing_municipalities(data) * 100
    print(percentage)
    print(f"Proportion of growing municipalities: {percentage:.1f}%")

if __name__ == "__main__":
    main()
