#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=";")
    df = df.dropna(how = "all")
    df = df.dropna(axis = 1, how = "all")
    df = df.iloc[:,0]
    df = df.str.split(expand=True)
    df.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    df['Hour'] = df['Hour'].str[0:2]

    weekdays = {
        "ma":"Mon",
        "ti":"Tue",
        "ke":"Wed",
        "to":"Thu",
        "pe":"Fri",
        "la":"Sat",
        "su":"Sun"
    }
    
    months = {
        "tammi" :1,
        "helmi" :2,
        "maalis" :3,
        "huhti" :4,
        "touko" :5,
        "kesä":6,
        "heinä" :7,
        "elo" :8,
        "syys" :9,
        "loka" :10,
        "marras" :11,
        "joulu" :12,
    }

    df = df.replace(weekdays, value = None)
    df = df.replace(months, value = None)
    df.iloc[:,1:] = df.iloc[:,1:].astype(int)
    return(df)


def main():
    print(split_date())
       
if __name__ == "__main__":
    main()
