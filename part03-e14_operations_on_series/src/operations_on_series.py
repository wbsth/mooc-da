#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    indices = ['a','b','c']
    s1 = pd.Series(L1, indices)
    s2 = pd.Series(L2, indices)
    return (s1, s2)
    
def modify_series(s1, s2):
    s1['d'] = s2['b']
    del s2['b']
    return (s1, s2)
    
def main():
    L1 = [1,2,3]
    L2 = [4,5,6]
    s1, s2 = create_series(L1, L2)
    s1mod, s2mod = modify_series(s1,s2)
    print(s1mod + s2mod)

if __name__ == "__main__":
    main()
