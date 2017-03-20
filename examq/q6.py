# Kirubel Tadesse
# Dr.Gordon Skelton
# J00720834
# Applied Programming 
# Jackson State University
# Computer Engineering Dept.

# 6. Write a program that is able to read in the data from the following file and display the count for each of the values.  Also, display the number of the elements in the file.  Use a dataframe to contain the data you read in from the file.


import pandas as pd
#import numpy as np

path = '/home/aniekan/Downloads/numbers2.csv'

# reading data from the file
df = pd.read_csv(path, names =['Data'])


# getting the shape of the data frame
print("printing the shape of the Dataframe is: ", df.shape)

# grouping each value and counts them
ecount = df.apply(pd.value_counts)

print("displaying Dataframe")
print( df)

#displaying the number of elements in the file 
print("The number of elements is: ", len(df.index))

#displaying the count of each of the values 
print("The frequency of each values are: ")
ecount.colume
print(ecount)


