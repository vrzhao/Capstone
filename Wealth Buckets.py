# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:43:51 2019

@author: Vincent Zhao
"""

import pandas as pd
import numpy as np

data = pd.read_csv("dataset_full.csv")
wealth = pd.read_excel("Wealth Buckets.xlsx")

data = data.set_index('Account Number').join(wealth.set_index('Account'))
data[data['label'] == 1]

def missing(x):
    if np.isnan(x):
        return 0
    else:
        return x

data['Index'] = data['Index'].transform(missing)

data.to_csv("data_wealth.csv")