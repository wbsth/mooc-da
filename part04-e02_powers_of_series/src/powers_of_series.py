#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    df = pd.DataFrame(index=s.index)
    for i in range(k):
        df[i+1] = [x**(i+1) for x in s]
    return(df)

def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()
