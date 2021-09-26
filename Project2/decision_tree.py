# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv

# I changed the path because the files are organized into traningfiles directory
dataSets = ['./trainingfiles/contact_lens_training_1.csv', './trainingfiles/contact_lens_training_2.csv',
            './trainingfiles/contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)

    # transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here
    for row in range(len(dbTraining)):
        X_r = []
        for col in range(len(dbTraining[row]) - 1):
            if dbTraining[row][col] == "Young":
                X_r.append(1)
            elif dbTraining[row][col] == "Presbyopic":
                X_r.append(2)
            elif dbTraining[row][col] == "Prepresbyopic":
                X_r.append(3)
            #     New attribute
            elif dbTraining[row][col] == "Myope":
                X_r.append(1)
            elif dbTraining[row][col] == "Hypermetrope":
                X_r.append(2)
            #     New attribute
            elif dbTraining[row][col] == "Yes":
                X_r.append(1)
            elif dbTraining[row][col] == "No":
                X_r.append(2)
            #     New Attribute
            elif dbTraining[row][col] == "reduced":
                X_r.append(1)
            elif dbTraining[row][col] == "Normal":
                X_r.append(2)
        X.append(X_r)
    print("Here is X:", X)

    # transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    # --> add your Python code here
    Y = [1 if row[-1] == "Yes" else 2 for row in dbTraining]
    print("Here is Y:", Y)

    # loop your training and test tasks 10 times here
    for i in range(10):
        # fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)

        # read the test data and add this data to dbTest
        # --> add your Python code here
        dbTest = []
        with open("./testfile/contact_lens_test.csv", "r") as testfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0:  # skipping the header
                    dbTest.append(row)

        print(dbTest)
    # for data in dbTest:
    # transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
    # class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
    # --> add your Python code here

    # compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
    # --> add your Python code here

    # find the lowest accuracy of this model during the 10 runs (training and test set)
    # --> add your Python code here

    # print the lowest accuracy of this model during the 10 runs (training and test set) and save it.
    # your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    # --> add your Python code here
