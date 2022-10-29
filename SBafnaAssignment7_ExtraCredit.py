#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 22:05:41 2022

@author: shantanubafna
"""
sum = 0 

for i in range(1000):
    if(i % 3 == 0 or i % 5 == 0):
        sum = sum + i
        
print(sum)