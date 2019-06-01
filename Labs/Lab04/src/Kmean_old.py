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
	

def distanceMeasure(dataPoint, centroid):
	return np.power(np.linalg.norm(dataPoint - centroid), 2) # np.sum(np.power(dataPoint - centroid, 2))
	
#
def kMean(data, k):
	# Inintialize
	# random k giá trị làm centroid_id và lấy ra các centroid initial
	initial_id = np.random.randint(100, size = k)
	
	# test voi 10 cluster nay
	# centroids = [[1,1,1,0,0,1,1,0], [1,1,0,1,0,0,1,1], [1,0,1,1,1,1,1,1], [1,0,1,0,0,1,1,1], 
	# 			[0,1,1,0,1,1,1,1], [0,0,0,1,1,0,1,1], [0,0,0,1,1,0,0,0], [1,0,1,0,0,0,1,1],
	# 			[1,1,1,0,0,0,1,0], [1,1,1,1,1,0,1,1]] 
	centroids = [[1,1,1,0,0,1,1,0], 
            [1,1,0,1,0,0,1,1], 
            [1,0,1,1,1,1,1,1]]
	# centroids = []
	# for id in initial_id:
	# 	centroids.append(data[id])	
	
	clusters = [[] for x in range(k)]  # Khởi tạo các cluster ban đầu là rỗng
	idCluster = np.zeros(len(data), dtype = int) # Khởi tạo các idCluster ban đầu của các điểm dữ liệu là 0
	iterations = 1 # khởi tạo số lần lặp ban đầu là 1
	
	while True:
		old_centroids = centroids
		id = 0
		# Xet cac dataPoint vao cac cluster tuong ung
		for dataPoint in data:
			distances = []
			for centroid in centroids:
				distances.append(distanceMeasure(dataPoint, centroid))
			idCluster[id] = np.argmin(distances)
			clusters[np.argmin(distances)].append(dataPoint)
			id += 1

		# Cập nhật centroids
		centroids = []
		for cluster in clusters:
			centroids.append(np.mean(cluster, axis = 0))

		# Nếu centroid không thay đổi thì dừng
		if np.array_equal(old_centroids, centroids) == True:
			break
		iterations += 1
		# reset lại các cluster để lặp
		clusters = [[] for x in range(k)] 

	print("Iters =", iterations)
	
	# test kết quả chạy thử
	# id = 0
	nCluster = []
	for cluster in clusters:
		# for el in cluster:
			# print(id, ":", el)
		nCluster.append(len(cluster))
		# print("So cluster", id, ":",len(cluster))
		# print(np.mean(cluster, axis = 0))
		# id += 1
	# Khởi tạo giá trị Sum of Squared Error
	SSE = 0 
	idData = 0
	for dataPoint in data:
		SSE += distanceMeasure(dataPoint, centroids[idCluster[idData]])
		# print(idCluster[idData], ":", dataPoint)
		idData += 1
	# print("SSE = ", SSE)
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
	output_model.write("Within cluster sum of squared errors: " + str(SSE) + "\n")
	# Ghi bảng các giá trị
	output_model.write("Cluster centroids:\n")
	output_model.write("\t\t\t\tCluster#\n")
	
	line1, line2 = "Attribute", "         "
	for i in range(len(nCluster)):
		line1 += "\t\t" + str(i)
		line2 += "\t\t" + str(nCluster[i])
	output_model.write(line1 + "\n")
	output_model.write(line2 + "\n")
	for i in range(len(name)):
		line = name[i]
		for centroid in centroids:
			line += "\t\t" + str(round(centroid[i], 4))
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