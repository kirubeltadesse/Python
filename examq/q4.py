# Kirubel Tadesse
# Dr.Gordon Skelton
# J00720834
# Applied Programming 
# Jackson State University
# Computer Engineering Dept.
#
#
#create a program that generates 10 random numbers between 0 and 100.  Use methods from numpy or any other library to produce the mean and standard deviation for the numbers.  Store the numbers in a list.


import numpy as np

count = 0
mylist=[]
while(count <10):
   num = np.random.randint(0,100)
   mylist.append(num)
   count = count + 1
print(mylist) 
