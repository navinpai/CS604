import datetime
import matplotlib.pyplot as plt

# make up some data
x = [i for i in range(100)]
y = [1.0/i for i in range(10,1010,10)]
z = [i/(i+9.0) for i in range(0,100)]

print y
# plot
plt.plot(x,y,color='r')
plt.plot(x,z,color='g')
# beautify the x-labels
#plt.gcf().autofmt_xdate()

plt.show()
