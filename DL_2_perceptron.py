# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:13:17 2020

@author: Hsun Jung Chen
"""

import numpy as np

# And Gate

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    temp = w1*x1 + w2*x2
    if temp <= theta:
        return 0
    elif temp > theta:
        return 1

print (AND(0, 0))
print (AND(1, 0))
print (AND(0, 1))
print (AND(1, 1))

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
print (w*x)
print (np.sum(w*x))
print (np.sum(w*x)+b)


# And Gate

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    temp = np.sum(w*x)+b
    if temp <= 0:
        return 0
    elif temp > 0:
        return 1
    
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.4, -0.4])
    b = 0.7
    temp = np.sum(w*x)+b
    if temp <= 0:
        return 0
    elif temp > 0:
        return 1

print (NAND(0, 0))
print (NAND(1, 0))
print (NAND(0, 1))
print (NAND(1, 1))



def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.4, 0.4])
    b = -0.2
    temp = np.sum(w*x)+b
    if temp <= 0:
        return 0
    elif temp > 0:
        return 1

print (OR(0, 0))
print (OR(1, 0))
print (OR(0, 1))
print (OR(1, 1))

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print (XOR(0, 0))
print (XOR(1, 0))
print (XOR(0, 1))
print (XOR(1, 1))








