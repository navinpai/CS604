import datetime
import matplotlib.pyplot as plt

# make up some data
x = [i for i in range(100)]
y = [0.5/(i+2.0) for i in range(9,909,9)]

print y
# plot
plt.plot(x,y)
# beautify the x-labels
#plt.gcf().autofmt_xdate()

plt.show()