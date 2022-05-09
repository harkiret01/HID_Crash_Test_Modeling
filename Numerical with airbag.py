# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:00:18 2022

@author: HARKIRET SINGH
"""
import math as m
import numpy as np
import scipy.integrate as integ
import matplotlib.pyplot as plt

def f1(t):
    if t == 74:
        return(22000/500)
    else:
        return (22000/(((t-74)*(t-74))+500))

def f2(d, t):
    return integ.quad(f1,t,(t+d))

def f3(d, t):
    result=f2(d, t)
    return (1/d*(result[0]))

def f4(d, t):
    return (d*(f3(d,t)**2.5))

x=[x for x in range(0,100)]
y=[ (f4(65.0, x)/1500) for x in range(0,100)]
y2=[ (f4(50.0, x)/1500) for x in range(0,100)]
y3=[ (f4(35.0, x)/1500) for x in range(0,100)]
y4=[ (f4(20.0, x)/1500) for x in range(0,100)]

fig, ax = plt.subplots()

ax.plot(x, y, 'purple', label="d=65")
ax.plot(x, y2, 'blue', label="d=50")
ax.plot(x, y3, 'green', label="d=35")
ax.plot(x, y4, 'red', label="d=20")
ax.set_title('With airbag')
ax.legend()
fig.tight_layout()

