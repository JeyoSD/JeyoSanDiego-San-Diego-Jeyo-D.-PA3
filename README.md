# Experiment 3: Python Data Analysis

This is a repository that contains Jupyter Notebook code using the Python programming language. It is a set of two exercises that make use of Python Data Analysis concepts.

## 1. First and Last Row Problem
This code loads a given dataframe called "cars.csv" using ```cars = pd.read_csv('cars.csv')``` and displays the first and last five rows of the dataframe by using a numpy code alongside the ```.iloc[]``` code to concatenate the sliced data from the first 0th to 5th rows and 27th to 32nd using ```cars_5rows = cars.iloc[np.r_[0:5, 27:32]]```.

### First and Last Row Code:
```
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
```

**Loaded Output:**
```
	Model	mpg	cyl	disp	hp	drat	wt	qsec	vs	am	gear	carb
0	Mazda RX4	21.0	6	160.0	110	3.90	2.620	16.46	0	1	4	4
1	Mazda RX4 Wag	21.0	6	160.0	110	3.90	2.875	17.02	0	1	4	4
2	Datsun 710	22.8	4	108.0	93	3.85	2.320	18.61	1	1	4	1
3	Hornet 4 Drive	21.4	6	258.0	110	3.08	3.215	19.44	1	0	3	1
4	Hornet Sportabout	18.7	8	360.0	175	3.15	3.440	17.02	0	0	3	2
27	Lotus Europa	30.4	4	95.1	113	3.77	1.513	16.90	1	1	5	2
28	Ford Pantera L	15.8	8	351.0	264	4.22	3.170	14.50	0	1	5	4
29	Ferrari Dino	19.7	6	145.0	175	3.62	2.770	15.50	0	1	5	6
30	Maserati Bora	15.0	8	301.0	335	3.54	3.570	14.60	0	1	5	8
31	Volvo 142E	21.4	4	121.0	109	4.11	2.780	18.60	1	1	4	2
```

## 2. Subsetting, Slicing, and Indexing Problem:
This code locates specific data from the cars.csv dataframe by first loading the given .csv file using ```cars2 = pd.read_csv('cars.csv')```, then first utilizing slicing to find the first five rows of odd-index columns using ```cars2.loc[0:4, ['Model', 'mpg', 'disp', 'drat', 'qsec', 'am', 'carb']]```. Second, the code utilized indexing to find the information of specific models of cars and specific information about certain models using ```cars2.loc[cars2['Model'] == 'Mazda RX4']``` and ```cars2.loc[cars2['Model'] == 'Camaro Z28', ['Model', 'cyl']]``` respectively. Lastly, it uses subsetting to find the cylinder and gear type from three particular car models from the dataframe using ```info = cars2.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]```.

### Divisible by 3 Code:
```
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
```

**Loaded Outputs:**
```
	Model	mpg	disp	drat	qsec	am	carb
0	Mazda RX4	21.0	160.0	3.90	16.46	1	4
1	Mazda RX4 Wag	21.0	160.0	3.90	17.02	1	4
2	Datsun 710	22.8	108.0	3.85	18.61	1	1
3	Hornet 4 Drive	21.4	258.0	3.08	19.44	0	1
4	Hornet Sportabout	18.7	360.0	3.15	17.02	0	2
```

```
Model	mpg	cyl	disp	hp	drat	wt	qsec	vs	am	gear	carb
0	Mazda RX4	21.0	6	160.0	110	3.9	2.62	16.46	0	1	4	4
```

```
Model	cyl
23	Camaro Z28	8
```

```
Model	cyl	gear
1	Mazda RX4 Wag	6	4
28	Ford Pantera L	8	5
18	Honda Civic	4	4
```

### Requirements:

• Python v.3.8 or later versions

• Jupyter Notebook

### How to Run:

**1.** Download the repository or make a fork through GitHub.

**2.** Open Jupyter Notebook and upload the file (.ipynb) using the notebook.

**3.** Run the cells.
