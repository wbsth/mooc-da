#!/usr/bin/env python3

import pandas as pd

def main():
    df = pd.read_csv("src/municipal.tsv", sep='\t')
    df_shape = df.shape
    print(f"Shape: {df_shape[0]},{df.shape[1]}")
    print("Columns:")
    for i in df.columns:
        print(i)

if __name__ == "__main__":
    main()
