# kirubel Tadesse
# Dr.Gordon Skelton
# J00720834
# Applied Programming 
# Jackson State University
# Computer Engineering Dept.




# 12. Write a function that will determine if a state is True or False.   The statement is “If a > b and b is not negative.”  You should return a boolean value to the main program and then have statement printed that says the statement is True or the statement is False.  Put the call to the function and the input statement in a while loop that will continue until you enter 99 for a.  The program will then display – Goodbye and Goodnight!!
a = 0
control = 1
def TOF(a,b):
   if ((int(a) >int( b)) and (int(b) > 0)):
      print("The statement is True ")    
      return True
   else:
      print("The statement is False")
   return False
while(control==1):
   a = input("Enter a value for a: ")
   b = input("Enter a value for b: ")
   TOF(a,b)
   if (int(a) == 99):
      control = 0
      print("Goodbye and Goodnight!")

 
