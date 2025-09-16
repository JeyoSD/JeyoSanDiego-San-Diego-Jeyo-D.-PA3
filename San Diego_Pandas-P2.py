#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Using the dataframe cars in problem 1, extract the following information using subsetting, slicing, and indexing operations.
#a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
#b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
#c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
#d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) the car models ‘Mazda RX4Wag’, ‘Ford Pantera L’, and ‘Honda Civic’ have.

import pandas as pd
def main():
    cars2 = pd.read_csv('cars.csv')
    
    cars_5odd = cars2.loc[0:4, ['Model', 'mpg', 'disp', 'drat', 'qsec', 'am', 'carb']] 
    display(cars_5odd)
    
    model = cars2.loc[cars2['Model'] == 'Mazda RX4']
    display(model)
    
    cyl = cars2.loc[cars2['Model'] == 'Camaro Z28', ['Model', 'cyl']]
    display(cyl)
    
    info = cars2.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]
    display(info)

main()
