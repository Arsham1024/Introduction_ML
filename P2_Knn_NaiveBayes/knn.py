#-------------------------------------------------------------------------
# AUTHOR: Arsham Mehrani
# FILENAME: kNN implementation
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv
import math
import numpy as np

db = []

#reading the data in a csv file
with open('trainingfiles/binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

def calculate_dist(a , b):
    return math.dist(a,b)

#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration.
    # For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    X = []
    temp = []

    # extracting an int format of x and y from each instance and saving it to a
    a = [int(x) for x in instance[:2]]  # instance[:2]
    # find the closest neightbor (1nn)
    for j in enumerate(db):

        b = [int(x) for x in j[1][:2]]

        # put the distance calculated into temp array to then be sorted
        temp.append([b, calculate_dist(a, b)])

    #  sort the array and print out the second item because the first is always going to be the node itself.
    temp.sort()
    print(temp)

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used
    # for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here
    # Y =

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    #testSample =

    #fitting the knn to the data
    # clf = KNeighborsClassifier(n_neighbors=1, p=2)
    # clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here

#print the error rate
#--> add your Python code here






