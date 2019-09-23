#!/usr/bin/env python3

import pandas as pd
import numpy as np

def cities():
    helsinki = ['Helsinki', 643272, 715.48]
    espoo = ['Espoo', 279044, 528.03]
    tampere = ['Tampere', 231853, 689.59]
    vantaa = ['Vantaa', 223027, 240.35]
    oulu = ['Oulu', 201810, 3817.52]
    
    cities_values = np.array([x[1:] for x in [helsinki, espoo, tampere, vantaa, oulu]])
    cities_names = np.array([x[0] for x in [helsinki, espoo, tampere, vantaa, oulu]])
    dataframe = pd.DataFrame(cities_values, columns=['Population', 'Total area'], index=cities_names)
    return dataframe
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()
