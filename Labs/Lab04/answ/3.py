import numpy as np

# Home, Products, Search, Prod_A, Prod_B, Prod_C, Cart, Purchase
centroids = np.array([
    [0.0938, 1, 0.375, 0.0313, 1, 0.6563, 0.4375, 0.2813], #1.1
    [0.7838, 0.6757, 0, 0.8919, 0.3784, 0.2162, 0.6757, 0.4324], #1.197
    [0.9032, 0.4839, 1, 0.6129, 0.2903, 0.5161, 0.7097, 0.4516] #0.716
])

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
print("#2")
new_2 = np.array([1, 0, 1, 0, 1, 0, 0, 0])
distances = []
for i in range(centroids.shape[0]):
    distances.append(np.linalg.norm(centroids[i] - new_2))
print("distances: ", distances)
print(np.argmin(distances))
print("Home, Products, Search, Prod_A, Prod_B, Prod_C, Cart, Purchase")
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
print("Home, Products, Search, Prod_A, Prod_B, Prod_C, Cart, Purchase")
printCentroid(centroids[np.argmin(distances)])
# 4.
print("===================================")
print("#3")
new_3 = [0, 1, 0, 0, 0, 1, 0, 0]
distances = []
for i in range(centroids.shape[0]):
    distances.append(np.linalg.norm(centroids[i] - new_2))
print("distances: ", distances)
print(np.argmin(distances))
print("Home, Products, Search, Prod_A, Prod_B, Prod_C, Cart, Purchase")
printCentroid(centroids[np.argmin(distances)])

