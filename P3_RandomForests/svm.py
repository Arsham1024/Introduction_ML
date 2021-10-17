#-------------------------------------------------------------------------
# AUTHOR: Arsham Mehrani
# FILENAME: SVM.py
# SPECIFICATION: Implement the best version of SVM
# FOR: CS 4210- Assignment #3
# TIME SPENT:
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import svm
from sklearn.metrics import accuracy_score
import csv

dbTest = []
X_training = []
Y_training = []
c = [1, 5, 10, 100]
degree = [1, 2, 3]
kernel = ["linear", "poly", "rbf"]
decision_function_shape = ["ovo", "ovr"]
highestAccuracy = 0

#reading the data in a csv file
with open('optdigits.tra', 'r') as trainingFile:
  reader = csv.reader(trainingFile)
  for i, row in enumerate(reader):
      # Each row is stored in an array.
      X_training.append(row[:-1]) #everything except for last element in each row because that is class.
      # one Dimension array
      Y_training.append(row[-1])  #here append that last thing in a class vector.

#reading the data in a csv file
with open('optdigits.tes', 'r') as testingFile:
  reader = csv.reader(testingFile)
  for i, row in enumerate(reader):
      dbTest.append(row[:-1])# test array is reading the class as well

print(len(dbTest[1]))

#created 4 nested for loops that will iterate through the values of c, degree, kernel, and decision_function_shape
#--> add your Python code here

for c_value in c: #iterates over c
    for degree_value in degree: #iterates over degree
        for kernel_value in kernel: #iterates kernel
           for dfs_value in decision_function_shape: #iterates over decision_function_shape

                #Create an SVM classifier that will test all combinations of c, degree, kernel, and decision_function_shape as hyperparameters. For instance svm.SVC(c=1)
                clf = svm.SVC(C=c_value, degree=degree_value, kernel=kernel_value, decision_function_shape=dfs_value)

                #Fit SVM to the training data
                clf.fit(X_training, Y_training)

                #make the classifier prediction for each test sample and start computing its accuracy
                #--> add your Python code here
                for test_case in dbTest:
                    class_predicted = clf.predict(dbTest)
                    print("here")
                print(accuracy_score(dbTest[-1] , class_predicted))

                #check if the calculated accuracy is higher than the previously one calculated. If so, update update the highest accuracy and print it together with the SVM hyperparameters
                #Example: "Highest SVM accuracy so far: 0.92, Parameters: a=1, degree=2, kernel= poly, decision_function_shape = 'ovo'"
                #--> add your Python code here











