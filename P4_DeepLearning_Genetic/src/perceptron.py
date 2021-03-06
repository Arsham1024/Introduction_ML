#-------------------------------------------------------------------------
# AUTHOR: Arsham Mehrani
# FILENAME: perceptron.py
# SPECIFICATION: implementation of a perceptron class
# FOR: CS 4210- Assignment #4
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: YOU HAVE TO WORK WITH THE PYTHON LIBRARIES numpy AND pandas to complete this code.

#importing some Python libraries
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier #pip install scikit-learn==0.18.rc2 if needed
import numpy as np
import pandas as pd


# Possible values for learning rate
n = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0]
# possible values for random state
r = [True, False]

P_accuracy = [] # perceptron accuracy array
MLP_accuracy = [] # Multi Layer Perceptron accuracy array

# highest accuracies so far
highest_P = 0
highest_MLP = 0

# ------------------ this is for training data ------------------
df = pd.read_csv('../Test_Train/optdigits.tra', sep=',', header=None) #reading the data by using Pandas library

X_training = np.array(df.values)[:,:64] #getting the first 64 fields to form the feature data for training
y_training = np.array(df.values)[:,-1]  #getting the last field to form the class label for training

# ------------------ this is for testing data ------------------
df = pd.read_csv('../Test_Train/optdigits.tes', sep=',', header=None) #reading the data by using Pandas library

X_test = np.array(df.values)[:,:64]    #getting the first 64 fields to form the feature data for test
Y_test = np.array(df.values)[:,-1]     #getting the last field to form the class label for test



for w in n: #iterates over n

    for b in r: #iterates over r

        for a in range(2): #iterates over the algorithms

            #Create a Neural Network classifier
            # if a == 0 train a perceptron
            if a==0:
               clf = Perceptron(eta0=w, shuffle=b, max_iter=1000) #eta0 = learning rate, random_state = shuffle the training data

            # if a == 1 train a multi layer perceptron with a single hidden layers with 25 neurons in that layer.
            else:
               clf= MLPClassifier(activation='logistic', learning_rate_init=w, hidden_layer_sizes=(25,), shuffle =b, max_iter=1000) #learning_rate_init = learning rate, hidden_layer_sizes = number of neurons in the ith hidden layer, random_state = shuffle the training data

            #Fit the Neural Network to the training data
            clf.fit(X_training, y_training)

            #make the classifier prediction for each test sample and start computing its accuracy
            #hint: to iterate over two collections simultaneously with zip() Example:
            #for (x_testSample, y_testSample) in zip(X_test, y_test):
            #to make a prediction do: clf.predict([x_testSample])
            #--> add your Python code here

            if a == 0:
                prediction_P = clf.predict(X_test)
                correct = 0
                # count the correct instances
                for i in range(len(prediction_P)):
                    if prediction_P[i] == Y_test[i]:
                        correct += 1
                # calculate current accuracy:
                accuracy_P = correct / len(prediction_P)

            else:
                prediction_MLP = clf.predict(X_test)
                correct = 0
                # count the correct instances
                for i in range(len(prediction_MLP)):
                    if prediction_MLP[i] == Y_test[i]:
                        correct += 1
                # calculate current accuracy:
                accuracy_MLP = correct / len(prediction_MLP)

            #check if the calculated accuracy is higher than the previously one calculated for each classifier. If so, update the highest accuracy and print it together with the network hyperparameters
            #Example: "Highest Perceptron accuracy so far: 0.88, Parameters: learning rate=0.01, random_state=True"
            #Example: "Highest MLP accuracy so far: 0.90, Parameters: learning rate=0.02, random_state=False"
            #--> add your Python code here


            try:
                if highest_P < accuracy_P:
                    highest_P = accuracy_P
                    print(f"Highest Perceptron accuracy so far: {highest_P}, Parameters: learning rate={w}, random_state={b}\n")

                if highest_MLP < accuracy_MLP:
                    highest_MLP = accuracy_MLP
                    print(f"Highest MLP accuracy so far: {highest_MLP}, Parameters: learning rate={w}, random_state={b}\n")
            except NameError:
                pass













