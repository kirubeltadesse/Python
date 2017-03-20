# kirubel Tadesse
# Dr.Gordon Skelton
# J00720834
# Applied Programming 
# Jackson State University
# Computer Engineering Dept.


# 11. Using the data from the numbers file, remove all of the duplicate numbers and print the list of only unique numbers.

import pandas as pd
# import numpy as np

# I have transposed the numbers.csv and resaved it as numbers2.csv
path = '/home/aniekan/Downloads/numbers2.csv'

# reading data from the file
df = pd.read_csv(path, names =['Data'] )

# removing the duplicate number and printing the list of only uunique numbers
print (df.drop_duplicates())
