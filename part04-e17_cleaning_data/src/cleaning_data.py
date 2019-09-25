#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv('src/presidents.tsv', sep="\t")
    
    # pres section
    pres = df['President']
    for cnt, val in enumerate(pres):
        if "," in val:
            val = val.replace(",","")
            val = val.split(" ")
            val = ' '.join(val[::-1])
            pres[cnt] = val
        else:
            pass
    df['President'] = pres   

    # startyear section
    df['Start'] = df['Start'].str[0:4].astype(int)

    # last section
    df.loc[0,'Last'] = None
    df['Last'] = df['Last'].astype(float)

    # seasons section
    dictio = {
        'two' : 2
    }
    df['Seasons'] = df['Seasons'].replace(dictio, value = None)
    df['Seasons'] = df['Seasons'].astype(int)

    # vce section
    vc = df["Vice-president"] #= df["Vice-president"].str.title()
    for cnt, val in enumerate(vc):
        val = val.title()
        if "," in val:
            val = val.replace(",","")
            val = val.split(" ")
            val = ' '.join(val[::-1])
        vc[cnt] = val

    df['Vice-president'] = vc
    #object, integer, float, integer, object
    return df

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
