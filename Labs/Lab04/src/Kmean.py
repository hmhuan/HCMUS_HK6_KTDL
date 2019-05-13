import sys
import csv
import numpy as np
from scipy.spatial.distance import cdist

# Đọc dữ liệu từ file input *.csv 
def read_input_file(fileIn_name):
	nameAttribute = []
	data = []
	with open(fileIn_name, 'r') as csvFile:
		reader = csv.reader(csvFile)
		line_count = 0
		for row in reader:
			if line_count == 0:
				nameAttribute = row
			else:
				val = []
				for el in row:
					val.append(int(el))
				data.append(np.array(val))
			line_count += 1
	csvFile.close()
	return nameAttribute, data
	

def distanceMeasurement(dataPoint, centroid):
	return np.sum(np.power(dataPoint - centroid, 2))
	
#
def kMean(data, k):
	# Inintialize
	# random k giá trị làm centroid_id và lấy ra các centroid initial
	initial_id = np.random.randint(100, size = k)
	#temp = np.array([1, 1, 1, 1, 1, 1, 1, 1])
	#centroids = [[1,1,1,0,0,1,1,0], [1,1,0,1,0,0,1,1]] # test voi 2 cluster nay
	centroids = []
	for id in initial_id:
		centroids.append(data[id])
	#for centroid in centroids:
	#	print(np.sum(np.power(centroid - temp, 2)))

	empty_cluster = [[] for x in range(k)]	
	
	clusters = empty_cluster
	idCluster = np.zeros(len(data), dtype = int)
	iterations = 0
	while True:
		old_centroids = centroids
		#print(old_centroids)
		clusters = [[] for x in range(k)]
		id = 0
		# Xet cac dataPoint vao cac cluster tuong ung
		for dataPoint in data:
			distances = []
			for centroid in centroids:
				distances.append(distanceMeasurement(dataPoint, centroid))
			idCluster[id] = np.argmin(distances)
			clusters[np.argmin(distances)].append(dataPoint)
			id += 1

		# Cap nhat centroid
		centroids = []
		for cluster in clusters:
			centroids.append(np.mean(cluster, axis = 0))
			
		# Neu centroid khong thay doi thi dung
		#if np.mean(np.absolute(np.array(old_centroids) - np.array(centroids))) < 0.0001:
		if np.array_equal(old_centroids, centroids) == True:
			break
		iterations += 1
	#print(centroids)
	print("Iters =", iterations)
	
	id = 0
	idData = 0
	nCluster = []
	for cluster in clusters:
		for el in cluster:
			print(id, ":", el)
		nCluster.append(len(cluster))
		print("So cluster", id, ":",len(cluster))
		print(np.mean(cluster, axis = 0))
		id += 1
	
	for dataPoint in data:
		print(idCluster[idData], ":", dataPoint)
		idData += 1
	
	return centroids, idCluster, nCluster

#
def write_output_asgn(output_asgn, name, data, idCluster):
	line = ""
	for el in name:		
		if el != name[len(name) - 1]:
			line += el + ", "
		else:
			line += el + ", "
	line += "Cluster\n"
	output_asgn.write(line)
	id = 0
	for dataPoint in data:
		line = ""
		for i in range(len(dataPoint)):
			if i != len(dataPoint) - 1:
				line += str(dataPoint[i]) + ", "
			else:
				line += str(dataPoint[i]) + ", "
		line += str(idCluster[id])+"\n"
		id += 1
		output_asgn.write(line)

def write_output_model(output_model, name, centroids, nCluster):
	
	# ghi SSE
	
	# Ghi bang
	output_model.write("Cluster centroids:\n")
	output_model.write("\t\t\tCluster#\n")
	
	line1, line2 = "Attribute", "         "
	for i in range(len(nCluster)):
		line1 += "\t" + str(i)
		line2 += "\t" + str(nCluster[i])
	output_model.write(line1 + "\n")
	output_model.write(line2 + "\n")
	for i in range(len(name)):
		line = name[i]
		for centroid in centroids:
			line += "\t" + str(round(centroid[i], 4))
		output_model.write(line + "\n")
	
	

def main():
	fileIn_name, output_model_name, output_asgn_name, k = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
	nameAttribute, data = read_input_file(fileIn_name)
	output_model = open(output_model_name, 'w')
	output_asgn = open(output_asgn_name, 'w')
	
	centroids, idCluster, nCluster = kMean(data, k)
	# ghi ra file assignment.csv
	write_output_asgn(output_asgn, nameAttribute, data, idCluster)
	write_output_model(output_model, nameAttribute, centroids, nCluster)
	
	output_model.close()
	output_asgn.close()
if __name__ == "__main__":
    # execute only if run as a script
    main()