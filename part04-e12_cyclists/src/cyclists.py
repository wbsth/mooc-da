#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=";")
    df_droprow = df.dropna(how = "all")
    df_dropcol = df_droprow.dropna(axis = 1, how = "all")
    return df_dropcol

def main():
    print(cyclists())

    
if __name__ == "__main__":
    main()
