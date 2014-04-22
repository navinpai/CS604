import datetime
import matplotlib.pyplot as plt

# make up some data
x = [i for i in range(100)]
y = [i/(i+9.0) for i in range(0,100)]

print y
# plot
plt.plot(x,y)
# beautify the x-labels
#plt.gcf().autofmt_xdate()

plt.show()
