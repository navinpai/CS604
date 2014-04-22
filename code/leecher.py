import datetime
import matplotlib.pyplot as plt

# make up some data
x = [i for i in range(100)]
y = [1.0/i for i in range(10,1010,10)]

print y
# plot
plt.plot(x,y,color='r')
# beautify the x-labels
#plt.gcf().autofmt_xdate()

plt.show()
