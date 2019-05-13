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
	temp = np.array([1, 1, 1, 1, 1, 1, 1, 1])
	centroids = []
	for id in initial_id:
		centroids.append(data[id])
	#for centroid in centroids:
	#	print(np.sum(np.power(centroid - temp, 2)))
	# empty cluster
	empty_cluster = [[] for x in range(k)]	
	
	#clusters = empty_cluster
	#for dataPoint in data:
	#	distances = []
	#	for centroid in centroids:
	#		distances.append(distanceMeasurement(dataPoint, centroid))
	#		#print(np.argmin(distances))
	#	clusters[np.argmin(distances)].append(dataPoint)
	#
	#id = 0
	#for cluster in clusters:
	#	for el in cluster:
	#		print(id, ":", el)
	#	print("So cluster", id, ":",len(cluster))
	#	print(np.mean(cluster, axis = 0))
	#	id += 1
	clusters = empty_cluster
	iterations = 0
	while True:
		old_centroids = centroids
		clusters = [[] for x in range(k)]
		# print(clusters)		
		for dataPoint in data:
			distances = []
			for centroid in centroids:
				distances.append(distanceMeasurement(dataPoint, centroid))
			# print(np.argmin(distances))
			clusters[np.argmin(distances)].append(dataPoint)
		centroids = []
		for cluster in clusters:
			centroids.append(np.mean(cluster, axis = 0))
		if np.mean(np.absolute(np.array(old_centroids) - np.array(centroids))) < 0.0001:
			break
		#print(iterations)
		iterations += 1
	print("Iters =", iterations)
	
	id = 0
	for cluster in clusters:
		count  = 0
		for el in cluster:
			print(id, ":", el)
			count += 1
		print("So cluster", id, ":",len(cluster))
		print(np.mean(cluster, axis = 0))
		id += 1
	
	return 0

#
def write_output_asgn(output_asgn, name, data):
	line = ""
	for el in name:		
		if el != name[len(name) - 1]:
			line += el + ", "
		else:
			line += el + "\n"
	output_asgn.write(line)
	for row in data:
		line = ""
		for i in range(len(row)):
			if i != len(row) - 1:
				line += str(row[i]) + ", "
			else:
				line += str(row[i]) + "\n"
		output_asgn.write(line)

def main():
	fileIn_name, output_model_name, output_asgn_name, k = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
	nameAttribute, data = read_input_file(fileIn_name)
	output_model = open(output_model_name, 'w')
	output_asgn = open(output_asgn_name, 'w')
	
	kMean(data, k)
	#a = np.array([1, 2])
	#b = np.array([2, 3])
	#print(np.array_equal(a, b))
	# ghi ra file assignment.csv
	write_output_asgn(output_asgn, nameAttribute, data)
	
	output_model.close()
	output_asgn.close()
if __name__ == "__main__":
    # execute only if run as a script
    main()