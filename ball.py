# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:54:24 2023

@author: sguzman24
"""

# y = v0*t - 0.5*g**2

def height (v0, t):
    g = 32.8
    y = v0*t -0.5*g*t**2
    return y
t = 1
while t > 0:
    v0 = input ('input velocity: ')
    v0 = float(v0)
    t = input('input time, sec: ')
    t = float (t)
    y = height(v0,t)
    print(f'after  {t} seconds height = {y}')
    """
at time 1.6 ball got to its max height which was about 38 feet. assuming we throw it vertically at intial velocity 50 fps
"""