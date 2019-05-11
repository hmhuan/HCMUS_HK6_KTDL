import numpy as np
import matplotlib.pyplot as plt
import math

# X la numFolds
X = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])

# Y1 la Accuracy voi unpruned = false
Y1 = np.array([89.1089, 93.0693, 89.1089, 94.0594, 89.1089, 88.1188, 90.099, 92.0792, 92.0792])

# Y2 la Accuracy voi unpruned = true
Y2 = np.array([92.0792, 92.0792, 92.0792, 92.0792, 92.0792, 92.0792, 92.0792, 92.0792, 92.0792])

plt.plot(X, Y1, X, Y2)
plt.ylabel('Accuracy')
plt.xlabel('numFolds')
plt.show()