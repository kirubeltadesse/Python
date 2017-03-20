# kirubel Tadesse
# Dr.Gordon Skelton
# J00720834
# Applied Programming 
# Jackson State University
# Computer Engineering Dept.

# 10. Write a program that uses the data from the numbers.csv file and sorts them in descending order.  You can print the modified list if you want.  The highest number is 10 and the lowest is 1.




import pandas as pd
# import numpy as np

# I have transposed the numbers.csv and resaved it as numbers2.csv
path = '/home/aniekan/Downloads/numbers2.csv'

# reading data from the file
df = pd.read_csv(path, names =['Data'] )

# pring the data from in a descending order
print ("Printing the frame in a descending order")
print (df.sort(['Data'], ascending = False))
