#!/usr/bin/python

__author__='Navin'

import datetime
import matplotlib.pyplot as plt

#Generate Data for seeding users
x = [i for i in range(100)]
y = [i/(i+9.0) for i in range(0,100)]

#print y
plt.plot(x,y,label='seeder')

plt.legend(loc='upper left')
#save plot as png
plt.savefig('img/plot-seeder.png')

#display plot
plt.show()
