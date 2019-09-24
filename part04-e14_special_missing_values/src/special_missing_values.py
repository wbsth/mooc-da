#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    existing = df[~df['LW'].isin(['New', 'Re'])]
    dropped = existing[existing['Pos'] > existing['LW'].astype(int)]
    return dropped

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
