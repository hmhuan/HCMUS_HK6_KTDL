import numpy as np
import matplotlib.pyplot as plt
import math

# X la numFolds
X = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])

# Y la Accuracy voi unpruned = false
Y1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

#
Y2 = np.array([3, 1, 9, 9, 0, 3, 2, 8, 10])

plt.plot(X, Y1, X, Y2)
plt.ylabel('Accuracy')
plt.xlabel('numFolds')
plt.show()