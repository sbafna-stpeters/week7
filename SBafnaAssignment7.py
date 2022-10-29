#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:47:43 2022

@author: shantanubafna
"""
import pandas as pd

def get_csv(web_link):
    dfr = pd.read_csv(web_link)
    return dfr

df = get_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.info()

import matplotlib.pyplot as plt

plt.hist(df["Age"], bins = 10)
plt.title("Age of Titanic Travellers")
plt.xlabel("Age")
plt.show()