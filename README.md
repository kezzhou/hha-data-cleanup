# hha-data-cleanup
# HHA 507 // Week 2 // Assignment 2

## This repo concerns using the Pandas package to import and reformat data for readibility. In this particular example, we use a dataset named "School Learning Modalities," taken from source: https://healthdata.gov/National/School-Learning-Modalities/aitj-yx37

## This repo contains a data folder, which contains subfolders raw and clean (denoting the nature of the data they contain). The untouched file version of "School Learning Modalities" is found in /hha-data-cleanup/data/raw. The scripts folder contains datacleanup.py which contains the script for modifying the data.

## In datacleanup.py we accomplish:
##      1. Loading in the dataset
##      2. Counting column and row number
##      3. Listing column names
##      4. Cleaning column names
##      5. Cleaning string values in each column
##      6. Assessing whitespace
##      7. Converting column dtypes appropriately where needed
##      8. Removing duplicate rows
##      9. Assess missing values
##      10. Creating new data (columns and values)