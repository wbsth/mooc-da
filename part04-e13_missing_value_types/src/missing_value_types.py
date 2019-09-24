#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    countries = ['United Kingdom', 'Finland', 'USA', 'Sweden', 'Germany', 'Russia']
    year_of_inpedence = [None, 1917, 1776,1523,None,1992]
    presidents = [None, 'Niinistö', 'Trump', None, 'Steinmeier', 'Putin']
    
    df = pd.DataFrame({'State':countries, 'Year of independence':year_of_inpedence, 'President':presidents}).set_index('State')
    return df
def main():
    missing_value_types()
    
if __name__ == "__main__":
    main()
