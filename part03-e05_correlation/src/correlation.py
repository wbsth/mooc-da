#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load2():
    """This loads the data from the internet. Does not work well on the TMC server."""
    import seaborn as sns
    return sns.load_dataset('iris').drop('species', axis=1).values

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    loaded_data = load()
    sepal_length = loaded_data[:,0]
    petal_length = loaded_data[:,2]
    return(scipy.stats.pearsonr(sepal_length, petal_length)[0])

def correlations():
    loaded_data = load()
    matrix = np.corrcoef(loaded_data, rowvar=False)
    return(matrix)

def main():
    pass

if __name__ == "__main__":
    main()
