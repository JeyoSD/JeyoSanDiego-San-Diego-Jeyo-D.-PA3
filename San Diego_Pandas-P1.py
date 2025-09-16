#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
def main():
    cars = pd.read_csv('cars.csv')
    
    cars_5rows = cars.iloc[np.r_[0:5, 27:32]]
    display(cars_5rows)
    
main()

