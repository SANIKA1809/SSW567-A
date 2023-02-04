# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 20:58:44 2023

@author: Sanika More
"""
import time
assignment=input("assignment name")

def my_brand():
    print("=*=*=*= Sanika More =*=*=*=")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*= ")
    print("=*=*=*="+ assignment +"=*=*=*= ")

    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

    print(time_string)


my_brand()


def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

# Function definition for type
def classify_triangle(a,b,c):
    if a==b and b==c:
        print('Triangle is Equilateral.')
    elif a==b or b==c or a==c:
        print('Triangle is Isosceles.')
    elif (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b):
        print('Triangle is right angle')
    else:
        print('Triangle is Scalane')

# Reading Three Sides
a = int(input('Enter length of side a: '))
b = int(input('Enter length of side b: '))
c = int(input('Enter length of side c: '))

# Function call & making decision
if is_valid_triangle(a, b, c):
    classify_triangle(a, b, c)
else:
    print("not triangle")