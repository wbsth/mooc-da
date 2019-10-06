#!/usr/bin/env python3

import pandas as pd


def top_bands():
    top = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    bands = pd.read_csv('src/bands.tsv', sep='\t')
    bands['Band'] = bands['Band'].str.upper()
    merged = pd.merge(top, bands, left_on=['Artist'], right_on=['Band'])
    return merged


def main():
    print(top_bands())


if __name__ == "__main__":
    main()
