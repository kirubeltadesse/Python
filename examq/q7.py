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
df = pd.read_csv(path, names =['Data'] )

largest = df.max()
smallest = df.min()

#producing the largest value
print'The largest value is: ', largest 

#producing the smallest value
print'The smallest value is: ', smallest 

















