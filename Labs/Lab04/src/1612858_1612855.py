import sys
import csv
import numpy as np
import math

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
	

def distanceMeasure(dataPoint, centroid):
	return np.sum(np.power(dataPoint - centroid, 2))
	#np.power(np.linalg.norm(dataPoint - centroid), 2) #
	
#
def kMean(data, k):
	"""
	Input: tập data và giá trị k số cluster.
	Output: 
		- Centroids: [] các centroid của cluster.
		- iDCluster: [] chứa giá trị id của cluster mà dataPoint thuộc về.
		- nCluster: [] chứa số lượng phần tử thuộc mỗi cluster.
		- SSE: giá trị Sum of Squared Error.
	"""
	# Inintialize
	# random k giá trị làm centroid_id và lấy ra các centroid initial
	#print(len(data))
	initial_id = np.random.choice(len(data), size = k, replace = False)	
	# centroids = [[1,1,1,0,0,1,1,0],
    #         [1,1,0,1,0,0,1,1],
    #         [1,0,1,1,1,1,1,1],
    #         [1,0,1,0,0,1,1,1],
    #         [0,1,1,0,1,1,1,1],
    #         [0,0,0,1,1,0,1,1],
    #         [0,0,0,1,1,0,0,0],
    #         [1,0,1,0,0,0,1,1]]
	
	centroids = []
	for id in initial_id:
		centroids.append(data[id])
		
	print("Initial starting points (random):\n")
	for i in range(len(centroids)):
		print("Cluster%d: " %i, centroids[i])
	print("\nProcessing...")
	# Khởi tạo các cluster ban đầu là rỗng
	clusters = [[] for x in range(k)]
	# Khởi tạo các idCluster ban đầu của các điểm dữ liệu là 0
	idCluster = np.zeros(len(data), dtype = int) 
	iterations = 1 # khởi tạo số lần lặp ban đầu là 1
	
	while True:
		pre_centroids = np.copy(centroids) #lưu lại centroids cũ
		SSE = 0
		print("Iteration %d:" % iterations)
		id = 0
		# Xet cac dataPoint vao cac cluster tuong ung
		#print("\tSample i: cluster")
		for dataPoint in data:
			distances = []
			for centroid in centroids:
				distances.append(distanceMeasure(dataPoint, centroid))
			idCluster[id] = np.argmin(distances)
			clusters[np.argmin(distances)].append(dataPoint)
			SSE += distances[idCluster[id]]
			id += 1
			#print("\tSample %d: %d" %(id, idCluster[id - 1]))
		print("SSE = ", SSE)
		print("---------------------------")
		# Cập nhật centroids
		centroids = []
		for cluster in clusters:
			if (len(cluster) != 0):
				centroids.append(np.mean(cluster, axis = 0))
			else:
				centroids.append(np.zeros(8))
		# delta = np.sum(np.abs(np.subtract(old_centroids, centroids)))
		# print(iterations,":", delta)
		# Nếu centroid không thay đổi thì dừng
		if np.array_equal(pre_centroids, centroids) == True:
			break
		#if ( delta < 0.0001): 
		#	break
		iterations += 1
		# reset lại các cluster để cho vòng lặp tiếp theo
		clusters = [[] for x in range(k)] 
	
	# test kết quả chạy thử
	nCluster = []
	for cluster in clusters:
		nCluster.append(len(cluster))

	# Khởi tạo giá trị Sum of Squared Error
	print("Calculating SSE value...")
	SSE = 0 
	idData = 0
	for dataPoint in data:
		SSE += distanceMeasure(dataPoint, centroids[idCluster[idData]])
		idData += 1
	print("Result:\nIterations = %s\nSSE value = %s" %(iterations, SSE))
	return centroids, idCluster, nCluster, SSE

# Hàm ghi ra file output assignment.csv
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

# Hàm ghi ra file output model.txt
def write_output_model(output_model, name, centroids, nCluster, SSE):
	
	# ghi SSE
	output_model.write("Within cluster sum of squared errors: %f \n" %(SSE))
	# Ghi bảng các giá trị
	output_model.write("Cluster centroids:\n")
	space = "\t\t" * int((len(centroids) / 2))
	output_model.write(space + "Cluster#\n")
	
	line1, line2 = "Attribute", "         "
	for i in range(len(nCluster)):
		line1 += "%10s" % i
		line2 += "%10s" % ("(" + str(nCluster[i]) + ")")
	output_model.write(line1 + "\n")
	output_model.write(line2 + "\n")
	output_model.write("==========" + "==========" * int((len(centroids))) + "\n")
	for i in range(len(name)):
		line = "%-9s" % name[i]
		for centroid in centroids:
			line += "%10s" % round(centroid[i], 4) #str(round(centroid[i], 4))
		output_model.write(line + "\n")
	
	
def main():
	# Đọc vào các parameters
	fileIn_name, output_model_name, output_asgn_name, k = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])

	# Đọc dữu liệu từ file input .csv
	nameAttribute, data = read_input_file(fileIn_name)
	
	# Mở 2 file output để ghi kết quả sau khi chạy
	output_model = open(output_model_name, 'w')
	output_asgn = open(output_asgn_name, 'w')

	# Chạy hàm kMean
	centroids, idCluster, nCluster, SSE = kMean(data, k)
	
	# ghi ra file assignment.csv và model.txt
	write_output_asgn(output_asgn, nameAttribute, data, idCluster)
	write_output_model(output_model, nameAttribute, centroids, nCluster, SSE)
	
	# Đóng 2 file để lưu
	output_model.close()
	output_asgn.close()
	
if __name__ == "__main__":
    # execute only if run as a script
    main()