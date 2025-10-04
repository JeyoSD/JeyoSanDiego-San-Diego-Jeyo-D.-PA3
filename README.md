# Experiment 3: Python Data Analysis v.1.1

This repository contains Jupyter Notebook code written in the Python programming language. It is a set of two exercises that utilize Python Data Analysis concepts.

## 1. First and Last Row Problem
The first part of the code imports the Pandas and NumPy Libraries using `import pandas as pd` and `import numpy as np` respectively, and reads the `cars.csv` file in the user's local files using `pd.read_csv()` to store the attached dataframe in `cars`.
```
import pandas as pd #Imports the Pandas Library
import numpy as np #Imports the Numpy Library
def main():
    cars = pd.read_csv('cars.csv') #Reads the cars.csv file in the user's files and stores the contained dataframe in cars
```
The next part of the code locates the first and last five rows of the `cars` dataframe using `.iloc[]`. The indexer has two main parts, consisting of `np.r_`,  which concatenates the two slices from the first (1st to 5th) and last (28th to 32nd) five rows of the dataframe using `[[0:5], [27:32]]`. It stores the dataframe in `cars_5rows` and outputs the dataframe using `display()` before calling the main function to run the code.
```
    cars_5rows = cars.iloc[np.r_[0:5, 27:32]] #Locates the first and last five slices of the dataframe and concatenates them into one dataframe stored in cars_5rows
    display(cars_5rows) #Outputs the cars_5rows dataframe
    
main()
```

### First and Last Row Code:
```
import pandas as pd #Imports the Pandas Library
import numpy as np #Imports the Numpy Library
def main():
    cars = pd.read_csv('cars.csv') #Reads the cars.csv file in the user's files and stores the contained dataframe in cars
    
    cars_5rows = cars.iloc[np.r_[0:5, 27:32]] #Locates the first and last five slices of the dataframe and concatenates them into one dataframe stored in cars_5rows
    display(cars_5rows) #Outputs the cars_5rows dataframe
    
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
The first part of the code imports the Pandas Library using `import pandas as pd` and reads the `cars.csv` file from the user's local files using `pd.read_csv()`, storing the resulting dataframe in `cars2`.
```
import pandas as pd #Imports the Pandas Library
def main():
    cars2 = pd.read_csv('cars.csv') #Reads the cars.csv file in the user's files and stores the contained dataframe in cars
```
This part of the code locates the first five rows of the dataframe and every other column, specifically the odd columns, that correspond with each row. The code achieves this by using the `.loc[]` indexer and slicing the first five rows with `[0:4]`. It then instructs pandas to include only the odd columns, which turn out to be the model, mpg, disp, drat, qsec, am, and carb, using a column selection list before storing all values located under `cars_5odd` and outputting the dataframe with `display()`.
```
    cars_5odd = cars2.loc[0:4, ['Model', 'mpg', 'disp', 'drat', 'qsec', 'am', 'carb']] #Locates the first to fifth rows with the specified columns
    display(cars_5odd) #Displays the cars_5odd dataframe
```
The second part of the code utilizes indexing alongside the `.loc` indexer to find specifically the row containing the Mazda RX4 model in the cars2 dataframe using `cars2['Model'] == 'Mazda RX4'`. It stores the dataframe into `model` and outputs the result with `display()`.
```
    model = cars2.loc[cars2['Model'] == 'Mazda RX4'] #Locates the row with Mazda RX4 under the model category
    display(model) #Displays the model dataframe
```
The code uses a similar method to find the row with the model of Camaro Z28 using `cars2['Model'] == 'Camaro Z28'` and specifies to output only the columns consisting of the model information and cyl information by specifying the column selection list of `['Model', 'cyl']` and storing the output in `cyl`. It then displays the resulting dataframe using `display()`.
```
    cyl = cars2.loc[cars2['Model'] == 'Camaro Z28', ['Model', 'cyl']] #Locates the row with Camaro Z28 under the model category and selects only the model and cyl values 
    display(cyl) #Displays the cyl dataframe
```
The code locates using `.loc[]` the rows with the model Mazda RX4 Wag, Ford Pantera L, and Honda Civic, utilizing the bitwise or operator `|` to combine the conditions and specifying the column selection list of `['Model', 'cyl', 'gear]`, storing the resulting dataframe in `info` and displaying it with `display()`. Finally, the main function is called to execute the code.  
```
    #Locates the rows with Mazda RX4 Wag, Ford Pantera L, and Honda Civic under the model category and selects only the model, cyl, and gear values 
    info = cars2.loc[(cars2['Model'] == 'Mazda RX4 Wag') | (cars2['Model'] == 'Ford Pantera L') | (cars2['Model'] == 'Honda Civic'), ['Model', 'cyl', 'gear']]
    display(info) #Displays the info dataframe

main()
```

### Divisible by 3 Code:
```
import pandas as pd #Imports the Pandas Library
def main():
    cars2 = pd.read_csv('cars.csv') #Reads the cars.csv file in the user's files and stores the contained dataframe in cars
    
    cars_5odd = cars2.loc[0:4, ['Model', 'mpg', 'disp', 'drat', 'qsec', 'am', 'carb']] #Locates the first to fifth rows with the specified columns
    display(cars_5odd) #Displays the cars_5odd dataframe
    
    model = cars2.loc[cars2['Model'] == 'Mazda RX4'] #Locates the row with Mazda RX4 under the model category
    display(model) #Displays the model dataframe
    
    cyl = cars2.loc[cars2['Model'] == 'Camaro Z28', ['Model', 'cyl']] #Locates the row with Camaro Z28 under the model category and selects only the model and cyl values 
    display(cyl) #Displays the cyl dataframe
    
    #Locates the rows with Mazda RX4 Wag, Ford Pantera L, and Honda Civic under the model category and selects only the model, cyl, and gear values 
    info = cars2.loc[(cars2['Model'] == 'Mazda RX4 Wag') | (cars2['Model'] == 'Ford Pantera L') | (cars2['Model'] == 'Honda Civic'), ['Model', 'cyl', 'gear']]
    display(info) #Displays the info dataframe

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
