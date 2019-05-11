import numpy as np
import matplotlib.pyplot as plt
import math

# set width of bar
barWidth = 0.25

X = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])

# Y1 la Accuracy voi unpruned = false
Y1 = np.array([89.1089, 93.0693, 89.1089, 94.0594, 89.1089, 88.1188, 90.099, 92.0792, 92.0792])

# Y2 la Accuracy voi unpruned = true
Y2 = np.array([92.0792])

# Set position of bar on X axis
r1 = np.arange(2 - barWidth / 2, len(Y1) + 2 - barWidth / 2)
r2 = [r1[1] + barWidth]


#plt.bar(X, Y1, width=barWidth, edgecolor='white', label='var1')
#plt.bar
plt.bar(r1, Y1, color='#7f6d5f', width=barWidth, edgecolor='white', label='pruned')
plt.bar(r2, Y2, color='#557f2d', width=barWidth, edgecolor='white', label='unpruned')
plt.xticks(X)
plt.ylabel('Accuracy')
plt.xlabel('numFolds')
plt.legend()
plt.show()
