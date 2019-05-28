import numpy as np 

temp = np.array([[0.9615, 0.6667  ,1,     0.8571,          0],
    [0.6923,     0.6667,          0,     0.5714,          1],
    [0.6538,          0,          1,     0.8571,     0.3214],
    [0.4615,      0.963,          1,     0.7143,          0],
    [0.3846,     0.4444,        0.8,     0.0714,          1],
    [0.5385,          0,        0.8,     0.5714,     0.6786],
    [0.4615,     0.6296,        0.8,          1,        0.5],
    [     0,     0.5185,        0.4,          1,     0.3214]])

centroids = temp.T

def printCentroid(centroid):
    print("Home: %12s" % centroid[0])
    print("Products: %8s" % centroid[1])
    print("Search: %10s" % centroid[2])
    print("Prod_A: %10s" % centroid[3])
    print("Prod_B: %10s" % centroid[4])
    print("Pord_C: %10s" % centroid[5])
    print("Cart: %12s" % centroid[6])
    print("Purchase: %8s" % centroid[7])
# 2.
new_2 = np.array([1, 0, 1, 0, 1, 0, 0, 0])
distances = []
for i in range(centroids.shape[0]):
    distances.append(np.linalg.norm(centroids[i] - new_2))
print("distances: ", distances)
print(np.argmin(distances))
printCentroid(centroids[np.argmin(distances)])
# 3. =================================
print("===================================")
print("#3")
new_3 = [0, 1, 0, 0, 0, 1, 0, 0]
distances = []
for i in range(centroids.shape[0]):
    distances.append(np.linalg.norm(centroids[i] - new_2))
print("distances: ", distances)
print(np.argmin(distances))
printCentroid(centroids[np.argmin(distances)])