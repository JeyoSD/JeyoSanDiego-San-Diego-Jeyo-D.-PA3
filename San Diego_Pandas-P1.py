#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Using knowledge obtained from the experiment and demonstrations:
#a. Load the corresponding .csv file into a data frame named cars using pandas
#b. Display the first five and last five rows of the resulting cars.

import numpy as np
import pandas as pd
def main():
    cars = pd.read_csv('cars.csv')
    
    cars_5rows = cars.iloc[np.r_[0:5, 27:32]]
    display(cars_5rows)
    
main()
