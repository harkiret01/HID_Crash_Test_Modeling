#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:11:28 2022

@author: jasmindersingh
"""
import math as m
import numpy as np
import scipy.integrate as integ
import matplotlib.pyplot as plt

def f1(t):
    t = (16400/((t-68)**2 + 400) + (1480/((t-93)**2 + 18)))
    return t

def f2(d, t):
    return integ.quad(f1,t,(t+d))

def f3(d, t):
    result=f2(d, t)
    return (1/d*(result[0]))

def f4(d, t):
    return (d*(f3(d,t)**2.5))

fig, ax1 = plt.subplots()

x=[x for x in range(0,110)]
y=[ (f4(65.0, x)/1500) for x in range(0,110)]
y2=[ (f4(50.0, x)/1500) for x in range(0,110)]
y3=[ (f4(35.0, x)/1500) for x in range(0,110)]
y4=[ (f4(20.0, x)/1500) for x in range(0,110)]

ax1.plot(x, y, 'purple', label="d=65")
ax1.plot(x, y2, 'blue', label="d=50")
ax1.plot(x, y3, 'green', label="d=35")
ax1.plot(x, y4, 'red', label="d=20")
ax1.set_title('Without airbag')
ax1.legend()

