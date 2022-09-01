#### Terminal Commands

'pip3 install pandas'

#### Import Packages

import pandas as pd ## for this exercise we'll only require pandas for its data handling capabilities


#### Loading in data

df = pd.read_csv('data/raw/School_Learning_Modalities.csv') ## here we use pandas .read_csv function to read our csv file located under data/raw
## we use relative path here for convenience
## we define df so we can use other functions with df later on, such as .shape

df ## we can visualize how the data appears by simply running df, which we have just defined

#### Printing column and row count

df.shape ## this will output column and row count in the format: (rows, columns)
## there are 741876 rows and 9 columns

#### Listing column names

df.columns 