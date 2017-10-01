"""
    author: rkopeinig
    script: Utils
    description: Using functions for Time-Series Analysis
    date: 09/30/2017
    version: 0.1
"""

import os, quandl, pickle
import numpy as np
import pandas as pd

# Get Data from Quandl
def get_data(quandl_id):
    '''Download and cache Quandl dataseries'''
    cache_path = '{}.pkl'.format(quandl_id).replace('/','-')
    print cache_path
    try:
        f = open(cache_path, 'rb')
        df = pickle.load(f)
        print('Loaded {} from cache'.format(quandl_id))
    except (OSError, IOError) as e:
        print('Downloading {} from Quandl'.format(quandl_id))
        df = quandl.get(quandl_id, returns="pandas")
        df.to_pickle(cache_path)
        print('Cached {} at {}'.format(quandl_id, cache_path))
    return df

# Mean calculation
def mean_calculation(df):
    df['Mean'] = (df['High'] + df['Low']) / 2
    return df

# Auto Correlation
def auto_correlation(x):
    x = np.asarray(x)
    y = x-x.mean()
    result = np.correlate(y, y, mode='full')
    result = result[len(result)//2:]
    result /= result[0]
    return result
