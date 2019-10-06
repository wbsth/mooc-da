#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    top = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    test = top.groupby('Publisher')
    a = test['WoC'].sum()
    a = a.sort_values(ascending=False)
    top_publisher = a.index[0]
    final_df = top[top.Publisher == top_publisher]
    return final_df


def main():
    print(best_record_company())

    

if __name__ == "__main__":
    main()
