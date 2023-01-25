# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:45:26 2023

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



