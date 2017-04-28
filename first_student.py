# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:54:56 2017

@author: gskel
"""

import os
import numpy as np
import pandas as pd


class student(object):
    def __init__(self):
        self.jnumber = input("JNumber: ")
        self.name = input("Name: ")
        
    def print_name(self):
        print('Name:',self.name)
        
    def print_jno_name(self):
        print("JNumber:",self.jnumber,' Name:',self.name)


class course(object):
    def __init__(self):
        self.jnumber = input('JNumber: ').upper()
        self.name = input('Name of Course: ').upper()
        self.hours = input('Number of Hours: ').upper()
        self.letter_grade = input('Letter Grade: ').upper()
    
    def print_course(self):
        print(self.name,self.hours,self.letter_grade)
        
list_of_students = []  

courses = pd.DataFrame()

courses = pd.DataFrame(columns=['JNo','Course','Hours','Grade'])

def menu():
    os.system('cls')
    print("Student Entry Program\n")
    print('(E)nter Students')
    print('(A)dd Courses')
    print('(D)isplay Students')
    print('(I)ndividual Student')
    print('(Q)uit')      

def enter_students():
    reply = 'y'
    while((reply == 'y') or (reply == 'Y')):
        student1 = student()
        list_of_students.append(student1)
        reply = input("Enter another student (y/n):  ")
        
def display_students():
    for item in range(len(list_of_students)):
        list_of_students[item].print_jno_name()
    x = input('End of List, Press Any Key to Return to Menu')
    x = ''
    
def individual_student(item):
    if item in list_of_students:
        list_of_students[0].print_jno_name()
        
def enter_course():
    reply = 'y'
    reply = reply.upper()
    while((reply == 'Y')):
        course1 = course()
        courses.loc[len(courses)]=[course1.jnumber,course1.name,course1.hours,course1.letter_grade] 
        reply = input("Enter another course (y/n):  ")

def display_menu():
    menu()

answer = ' '
while answer != 'Q':
    display_menu()
    answer = input("Enter Desired Option:")
    answer = answer.upper()
    if answer == 'E':
        os.system('cls')
        enter_students()
    if answer == 'D':
        os.system('cls')
        display_students()
    if answer == 'I':
        os.system('cls')
        jay_number = input("Enter Student's JNumber")
        individual_student(jay_number)
    if answer == 'A':
        os.system('cls')
        enter_course()
    
print(courses)
courses.to_csv('c:/users/gskel/courses')

        

