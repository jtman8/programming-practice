#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:42:00 2020

@author: tylermanderfield
"""

a = input("Give me a word, any word: ")
while a.isalpha() == False:
    a = input("I said a word! Try again. Give me a word, any word: ")
print("Hey! " + a.capitalize() + " is a cool word!")