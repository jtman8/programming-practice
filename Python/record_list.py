#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:49:56 2020

@author: tylermanderfield
"""
## First Try
a = input("What are your three favorite things in life? (Separate them with commas)")
a = a.split(",")
for item in a:
    print(item.strip())

## Alternative
print("What are your three favorite things in life?")
li = []
for i in range(1,4):
    li.append(input(str(i) + ": "))
for i in li:
    print(i.strip())