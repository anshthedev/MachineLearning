import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt

year = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
christian = [77, 76, 75, 73, 73, 71, 69, 68, 67, 65]
unaffiliated = [17, 17, 19, 19, 20, 21, 24, 23, 25, 26]

plt.plot(year, christian);
plt.plot(year, unaffiliated);
plt.ylim(0, 80);
plt.plot(year, christian, label='Christian')
plt.plot(year, unaffiliated, label='Unaffiliated')
plt.xlim(year[0], year[-1])
plt.legend()
plt.show()
