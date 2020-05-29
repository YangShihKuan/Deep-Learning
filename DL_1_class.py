# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:14:08 2020

@author: Hsun Jung Chen
"""
import numpy as np

class Man:
    def __init__(self,name):
        self.name = name
        print("Initilized")
        
    def hello(self):
        print("Hello " + self.name + " !")
    def goodbye(self):
        print("Good-bye " + self.name + " !")

m = Man("David")
m.hello()
m.goodbye()

name_list = ['a', 'b']
x = [Man(i) for i in name_list]

for i in range(len(name_list)):
    print(x[i].name)
    x[i].goodbye()