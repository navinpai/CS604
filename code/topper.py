#!/usr/bin/python

__author__='Navin'

import datetime
import matplotlib.pyplot as plt

#Generate data for leecher
x = [i for i in range(100)]
y = [0.5/(i+2.0) for i in range(9,909,9)]

#print y
plt.plot(x,y,color='b')


#save plot as png
plt.savefig('img/plot-top.png')

plt.show()
