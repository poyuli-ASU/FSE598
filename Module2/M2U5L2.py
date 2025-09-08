import statistics  # Import statistics module for statistical calculations
import numpy as np  # Import numpy for numerical operations and arrays
import matplotlib.pyplot as plt  # Import matplotlib for plotting graphs
import csv 

def main():  # Define the main function
    m1 = np.array([
        [1,2,3,4],
        [4,5,6,7],
        [7,8,9,10],
        [10,11,12,13]]) # no type is default
    m2 = np.array([
        [1,2,3,4],
        [4,5,6,7],
        [7,8,9,10],
        [10,11,12,13]], dtype=float) # float
    m3 = np.array([ 
        [1,2,3,4],
        [4,5,6,7],
        [7,8,9,10],
        [10,11,12,13]], dtype=str) # str
    m4 = m1+m2
    # WAY1 
    with open('Module2/data.csv', newline='') as csvfile:
        myData = csv.reader(csvfile, delimiter=',')
        for row in myData:
            print(row)
    #WAY2 
    data = np.genfromtxt('Module2/data.csv', delimiter=',', skip_header=1)
    print(data)
    print('\n')
    for r in data:
        print(r)
    print('\n')
    row = [fields for fields in data]
    print(row[0][0:3], '\n')
    print(row[1][0:3], '\n')
    print(row[2][0:3], '\n')

if __name__ == "__main__":  
    main() 
