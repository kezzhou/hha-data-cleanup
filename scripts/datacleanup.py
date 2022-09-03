#### Terminal commands ####

'pip3 install pandas'



#### Import packages ####

import pandas as pd ## for this exercise we'll most rely on pandas for its data handling capabilities
import numpy as np ## numpy for missing data


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

df[cols] = df[cols].apply(lambda x: x.str.lower()) ## converting string values to lowercase

df[cols] = df[cols].apply(lambda x: x.str.strip()) ## we use df.apply and lambda x here to apply the str.strip function to all selected objects

df.head ## we can use df.head or df.sample or any other visualizing command to help us check progress

df[cols] = df[cols].apply(lambda x: x.str.replace('[^A-Za-z0-9]+', '_')) ## IT IS RECOMMENDED TO RUN THIS LINE AFTER LINE 80 AS IT WILL MESS WITH DATETIME CONVERSION
## this will replace special characters in cells with underscore



#### Assessing whitespace and special characters

print(df[cols].apply(lambda x: x.str.count('[^A-Za-z0-9]+'))) ## counting special characters in every string-based cell

print(df[cols].apply(lambda x: x.str.count(' '))) ## counting whitespace in every string-based cell




#### Converting column types appropriately ####

df.dtypes ## this lists each column name and its corresponding dtype

df.sample ## we can then use df.sample or an vs code extension to preview the csv and judge if the elements' dtypes are appropriate

df['week'] = pd.to_datetime(df['week']) ## it looks like 'week' is the only odd one out with its format as string despite it being datetime.
## there is a time value present as well but it seems to be 12:00:00 AM for all rows. we can safely exclude that portion and go ahead with datetime

df.dtypes ## to check our work

df.sample

#### Finding duplicate rows and removing them ####

df.duplicated(keep='first') ## this labels all 'first' occurence of rows as unique (boolean value false) and all duplicate occurences after that as duplicate (boolean value true)

df.drop_duplicates(keep=False) ## this function drops all duplicates based on parameters. in this case keep is labeled false so that no instance of duplicates are kept

## it seems like this dataset has no duplicates because the row number did not change. still, it is a good measure to take



#### Assess missing data ####

df.isnull().count() ## provides a count of missing values in each column

df.replace(to_replace='', value=np.nan, inplace=True) ## replacing empty cells with NaN with numpy

df.replace(to_replace=' ', value=np.nan, inplace=True) ## replacing cells with whitespace with NaN

df.sample ## check our work



#### Creating new data ####

df['modality_inperson'] = (df['learning_modality'].apply(lambda x: 'true' if x == 'in_person' else 'false')) ## here we create a new column named modality_inperson which is based off the value of learning_modality
## rows with value 'in_person' will see a corresponding cell in the new column with value 'true'

df.to_csv('data/clean/school_learning_modalities_mod.csv') ## we burn our results into a new csv under /data/clean