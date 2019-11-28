# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 23:02:32 2019

@author: Chris Man - University of Leeds - MSc GIS
"""

import csv
import matplotlib.pyplot

env = []
f = open('in.txt')
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset:
    envrow = []
    for value in row:
       envrow.append(value)
    env.append(envrow)
f.close()

matplotlib.pyplot.imshow(env)
matplotlib.pyplot.show()
