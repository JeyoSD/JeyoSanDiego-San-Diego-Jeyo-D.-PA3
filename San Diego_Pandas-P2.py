#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
def main():
    cars2 = pd.read_csv('cars.csv')
    
    cars_5odd = cars2.loc[[0, 1, 2, 3, 4], ['mpg', 'disp', 'drat', 'qsec', 'am', 'carb']] 
    display(cars_5odd)
    
    model = cars2.loc[cars2['Model'] == 'Mazda RX4']
    display(model)
    
    cyl = cars2.loc[cars2['Model'] == 'Camaro Z28', ['Model', 'cyl']]
    display(cyl)
    
    info = cars2.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]
    
    display(info)

main()

