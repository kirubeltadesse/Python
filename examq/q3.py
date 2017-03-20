# Kirubel Tadesse
# Dr.Gordon Skelton
# J00720834
# Applied Programming 
# Jackson State University
# Computer Engineering Dept.

#create a program that uses a function to determine the larger of two numbers and return the larger to the main body of the program and then print it.  You have to enter the numbers from the keyboard so you have to use input.

#defining the function
def printLarg():
   x = input("Enter your first number: ")
   y = input("Enter your second number: ")
   holder=[x,y]
   larg = max(holder)
   print("the larger number is : ")
   print(larg)
   return larg

#calling the function
printLarg()
