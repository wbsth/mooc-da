#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    return pd.Series(s.index.values, s.values)

def main():
    series = pd.Series(['a','b','c'])
    print(inverse_series(series))

if __name__ == "__main__":
    main()
