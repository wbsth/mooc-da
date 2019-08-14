#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    ret_list = []
    for row in a:
        ret_list.append(row)
    return ret_list

def get_columns(a):
    ret_list = []
    for column in a.T:
        ret_list.append(column)
    return ret_list

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
