#-------------------------------------------------------------------------
# AUTHOR: Arsham Mehrani
# FILENAME: Find S algorithm implementation
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('input_files/contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
##--> add your Python code here

print("\nFinding all the positive samples:")
positive_h = []
for row in db:
    if row[-1] == "Yes":
        positive_h.append(row)

# delete the class column
[row.pop(-1) for row in positive_h]

# Now step two generalizing the hypothesis:
for row in positive_h:
    i = 0
    for item in row:
        # first scenario where it is 0 we are comparing to
        if hypothesis[i] == '0':
            hypothesis[i] = item
            i+=1
        # second scenario where the value of h is not 0
        elif not hypothesis[i] == str(item):
            hypothesis[i] = "?"


#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
##--> add your Python code here

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)