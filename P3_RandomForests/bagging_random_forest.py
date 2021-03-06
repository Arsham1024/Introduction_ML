# -------------------------------------------------------------------------
# AUTHOR: Arsham Mehrani
# FILENAME: bagging_random_forest
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #3
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn import tree
from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier
import csv

dbTraining = []
dbTest = []
X_training = []
Y_training = []
classVotes = []  # this array will be used to count the votes of each classifier
# class_predicted = []
X_test = []
Y_test = []

# reading the training data in a csv file
with open('optdigits.tra', 'r') as trainingFile:
    reader = csv.reader(trainingFile)
    for i, row in enumerate(reader):
        dbTraining.append(row)

# reading the test data in a csv file
with open('optdigits.tes', 'r') as testingFile:
    reader = csv.reader(testingFile)
    for i, row in enumerate(reader):
        dbTest.append(row)
        classVotes.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])  # inititalizing the class votes for each test sample

    print("Started my base and ensemble classifier ...")

    for k in range(
            20):  # we will create 20 bootstrap samples here (k = 20). One classifier will be created for each bootstrap sample

        bootstrapSample = resample(dbTraining, n_samples=len(dbTraining), replace=True)
        # populate the values of X_training and Y_training by using the bootstrapSample
        for sample in bootstrapSample:
            # for each sample take class put it in Y and the rest in x
            X_training.append(sample[:-1])
            Y_training.append(sample[-1])

        # fitting the decision tree to the data
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=None)  # we will use a single decision tree without pruning it
        clf = clf.fit(X_training, Y_training)

        correct_sample = 0  # for accuracy
        for i, testSample in enumerate(dbTest):
            # make the classifier prediction for each test sample and update the corresponding index value in classVotes. For instance,
            # if your first base classifier predicted 2 for the first test sample, then classVotes[0,0,0,0,0,0,0,0,0,0] will change to classVotes[0,0,1,0,0,0,0,0,0,0].
            # Later, if your second base classifier predicted 3 for the first test sample, then classVotes[0,0,1,0,0,0,0,0,0,0] will change to classVotes[0,0,1,1,0,0,0,0,0,0]
            # Later, if your third base classifier predicted 3 for the first test sample, then classVotes[0,0,1,1,0,0,0,0,0,0] will change to classVotes[0,0,1,2,0,0,0,0,0,0]
            # this array will consolidate the votes of all classifier for all test samples

            # print("value predicted: ",  int(clf.predict([testSample[:-1]])))
            # print("value predicted1: ",  int(clf.predict([testSample[:-1]])[0]))

            # take each instance of test sample not including last one,
            # print(testSample[:-1])
            # print(type(clf.predict([testSample[:-1]])))
            value_prediction = int(clf.predict([testSample[:-1]])) # need to turn <class 'numpy.ndarray'> into int

            # print(classVotes[0])
            # in class votes on the correct row add 1 to that vote.
            classVotes[i][value_prediction] += 1

            if k == 0:  # for only the first base classifier, compare the prediction with the true label of the test sample here to start calculating its accuracy
                correct_sample += 1 * (value_prediction == int(testSample[-1])) #if value prediction matches ground truth we have correct sample

        if k == 0:  # for only the first base classifier, print its accuracy here
            accuracy = correct_sample / len(dbTest)
            print("Finished my base classifier (fast but relatively low accuracy) ...")
            print("My base classifier accuracy: " + str(accuracy))
            print("")

    # now, compare the final ensemble prediction (majority vote in classVotes) for each test sample with the ground truth label to calculate the accuracy of the ensemble classifier (all base classifiers together)
    correct_sample = 0  # reseting correctGuess
    for i, testSample in enumerate(dbTest):
        majority_vote = int(classVotes[i].index(max(classVotes[i]))) # each row classVotes[i], so select the maximum number/vote then return index for each row find the maximum vote and return the index
        correct_sample += 1 * (1 if majority_vote == int(testSample[-1]) else 0) # if the class predicted by majority vote matches ground truth then +1 to sample else 0

    # printing the ensemble accuracy here
    ensemble_accuracy = correct_sample / len(dbTest)
    print("Finished my ensemble classifier (slow but higher accuracy) ...")
    print("My ensemble accuracy: " + str(ensemble_accuracy))
    print("")


    # Random forest here:
    print("Started Random Forest algorithm ...")

    # Create a Random Forest Classifier
    clf = RandomForestClassifier(n_estimators=20)  # this is the number of decision trees that will be generated by Random Forest. The sample of the ensemble method used before
    # Fit Random Forest to the training data
    clf.fit(X_training, Y_training)

    # make the Random Forest prediction for each test sample. Example: class_predicted_rf = clf.predict([[3, 1, 2, 1, ...]]
    correct_sample = 0
    for i, testSample in enumerate(dbTest):
        value_prediction_fromRF = int(clf.predict([testSample[:-1]]))

        # compare the Random Forest prediction for each test sample with the ground truth label to calculate its accuracy
        correct_sample += 1 * (value_prediction_fromRF == int(testSample[-1])) # does prediction match ground truth?

    # printing Random Forest accuracy here
    RF_accuracy = correct_sample / len(dbTest)
    print("Random Forest accuracy: " + str(RF_accuracy))

    print("Finished Random Forest algorithm (much faster and higher accuracy!) ...")
