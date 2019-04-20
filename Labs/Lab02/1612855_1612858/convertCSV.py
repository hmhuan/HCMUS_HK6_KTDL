"""
Author: Minh Huan Huynh
Date: 17/04/2019
Reference resource: Mr.Xuan Hong Ong - https://ongxuanhong.wordpress.com/2015/08/24/apriori-va-fp-growth-voi-tap-du-lieu-plants/
"""
import sys

# init files
state_file = "stateabbr_filter.txt"
plants_data = "plants.data"
plants_binary = "plants.csv"

# function to load states in file "stateabbr_filter.txt"
def loadStates():
	states = []
	f = open(state_file, "r")
	for line in f:
		states.append(line.strip().split(" ")[0])
	
	f.close()
	return states

def convertToBinary():
    states = loadStates()
    fIn = open(plants_data, "r")
    fOut = open(plants_binary, "w")

    header = "name of plant"
    for state in states:
        header += "," + state
    fOut.write(header + "\n")
    for line in fIn:
        plantInfo = line.strip().split(",")
        newLine = plantInfo[0]
        for state in states:
            if state in plantInfo:
                newLine += ",y"
            else:
                newLine += ",n"
        fOut.write(newLine + "\n")
    fIn.close()
    fOut.close()
def main():
    convertToBinary()

if __name__ == "__main__":
    main()