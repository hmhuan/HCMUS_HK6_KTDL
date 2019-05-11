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
	

#
def kMean(data, k):
	# random k giá trị làm centroid
	
	return 0

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
	fileIn_name, output_model_name, output_asgn_name, k = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
	nameAttribute, data = read_input_file(fileIn_name)
	output_model = open(output_model_name, 'w')
	output_asgn = open(output_asgn_name, 'w')

	
	# ghi ra file assignment.csv
	write_output_asgn(output_asgn, nameAttribute, data)
	
	output_model.close()
	output_asgn.close()
if __name__ == "__main__":
    # execute only if run as a script
    main()