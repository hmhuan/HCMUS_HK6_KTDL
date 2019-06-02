import numpy as np 

temp = np.array([
[0.9048,          1,          1,          1,          0,          0,     0.8235], #Home
[0.9048,     0.9375,          0,     0.2857,          1,     0.1429,     0.4118], #Products
[0.7143,      0.125,          1,          1,     0.3214,     0.1429,     0.2941], #Search
[0.7619,      0.875,          1,     0.1429,          0,          1,     0.6471], #Prod_A
[ 0.381,     0.4375,          1,          0,          1,     0.2857,     0.3529], #Prod_B
[0.9048,      0.125,       0.75,     0.2857,     0.6786,          0,          0], #Prod_C
[0.6667,          1,       0.75,          1,        0.5,          1,          0], #Cart
[0.1905,     0.8125,        0.5,     0.7143,     0.3214,     0.8571,          0]])#Purchase

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
    distances.append(np.linalg.norm(centroids[i] - new_3))
print("distances: ", distances)
print(np.argmin(distances))
printCentroid(centroids[np.argmin(distances)])