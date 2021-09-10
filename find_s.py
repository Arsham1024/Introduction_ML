# -------------------------------------------------------------------------
# AUTHOR: Arsham Mehrani
# FILENAME: Find S algorithm implementation
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

# reading the data in a csv file
with open('input_files/contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes  # representing the most specific possible hypothesis
print(hypothesis)

# find the first positive training data in db and assign it to the vector hypothesis
##--> add your Python code here

# Positive_h is a list that holds all the positive samples of the original hypothesis
positive_h = []
for row in db:
    # grabbing the positive samples
    if row[-1] == "Yes":
        positive_h.append(row)

# delete the class column
[row.pop(-1) for row in positive_h]

# find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
##--> add your Python code here

# Now step two generalizing the hypothesis:
for row in positive_h:
    for i in range(len(row)):
        # first scenario where it is 0 we are comparing to
        # This condition is only going to apply to the first sample being examined.
        if hypothesis[i] == '0':
            hypothesis[i] = row[i]

        # second scenario where the value of h is not 0
        # This condition is going to apply to sample 2 and on.
        elif not hypothesis[i] == str(row[i]):
            hypothesis[i] = "?"

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)
