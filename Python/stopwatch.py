#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:30:59 2020

@author: tylermanderfield
"""

## Standard Implementation
from datetime import datetime

def function_something():
    a = []
    for i in range(1000000):
        a.append(i)
    return a

# find time before running my function
start_time = datetime.now()
function_something()
# print difference in time between after completion and start time
print(datetime.now() - start_time)


## In an iPython Shell, %timeit is a special function producing similar results
## however timeit runs it more than once and establishes an mean/sd of a 
## function's runtime
import timeit
%timeit function_something()