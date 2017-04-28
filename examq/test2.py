# kirubel Tadesse
# Dr.Gordon Skelton
# J00720834
# Applied Programming 
# Jackson State University
# Computer Engineering Dept.


# Write a program that uses the same file. Have that program produce the largest and smallest value from the file.  You can just modify the program in No. 6 above to solve this problem.

import pandas as pd
# import numpy as np

# I have transposed the numbers.csv and resaved it as numbers2.csv
path = '/home/aniekan/Downloads/numbers2.csv'

# reading data from the file
df = pd.read_csv(path, names=['Data','Index'])

###k = df.set_index(['columens',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]]) 

#print(k)
#print(len(k))
#for i, row in k.iterrows():
#    print(i)

#for i in k:
#s = pd.Series(k, index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

df1 = df.reset_index()
print("value of df1")
print(df1)
print("value of k")
#print(k.head())
print("value of df1 tail")
print(df1.tail(2))
print("value of df max")
print(df.max())
print("checking ")
print(df1.head())



















