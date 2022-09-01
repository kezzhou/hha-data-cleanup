#### Terminal commands ####

'pip3 install pandas'



#### Import packages ####

from itertools import count
import pandas as pd ## for this exercise we'll only require pandas for its data handling capabilities



#### Loading in data ####

df = pd.read_csv('data/raw/School_Learning_Modalities.csv') ## here we use pandas .read_csv function to read our csv file located under data/raw
## we use relative path here for convenience
## we define df so we can use other functions with df later on, such as .shape

df ## we can visualize how the data appears by simply running df, which we have just defined



#### Printing column and row count ####

df.shape ## this will output column and row count in the format: (rows, columns)
## there are 741876 rows and 9 columns



#### Listing column names ####

df.columns ## outputs list of column names



#### Cleaning column names and assessing white space and special characters ####

## based on the last function we ran, we saw a couple of unconventional naming standards applied to the column names
## there is capitalization and white space and possibly special characters

df.columns = df.columns.str.lower() ## we start by making column names uniformly lowercase

df.columns ## we intermittently run df.columns to check that our changes have anchored

df.columns = df.columns.str.replace(' ', '_') ## next we replace whitespace with underscore

df.columns

df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') ## finally, as a safety measure, we replace all special characters (that we may not see) with underscore

df.columns



#### Cleaning column strings ####

cols = df.select_dtypes(object).columns ## here we select all string types in all columns in preparation for purging whitespace and special characters in all of them

df[cols] = df[cols].apply(lambda x: x.str.strip()) ## we use df.apply and lambda x here to apply the str.strip function to all selected objects

df.head ## we can use df.head or df.sample or any other visualizing command to help us check progress

df[cols] = df[cols].apply(lambda x: x.str.replace('[^A-Za-z0-9]+', '_') ## we use df.apply again with str.replace to take care of special characters and replace them with underscore

df.head

df[cols] =df[cols].apply(lambda x: x.str.count('[^A-Za-z0-9]+'))

df['week'] = df['week'].str.count('[^A-Za-z0-9]+')


#### Converting column types appropriately ####


