#-------------------------------------------------------------------------
# AUTHOR: Arsham Mehrani
# FILENAME: decision_tree
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #1
# TIME SPENT: 3 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('input_files/contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append(row)
         print(row)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =

# Run through every col and pick out the unique elements to assign numbers to
for col in range(len(db[:4])):
    # reset temp for every col
    temp =[]
    dict =  {}
    i = 1
    for row in range(len(db)):
        # if the element is in temp then that means we already accounted for it.
        # put the unique element in the dictionary with unique ID
        if not db[row][col] in temp:
            temp.append(db[row][col])
            dict[db[row][col]] = i
            i+=1
    # Because dictionary elements are all unique I can use that to give keys to each unique value in each col
    # column array is to store every element in a column so that it can be appended to X
    # without this X would be a 1D array
    column = []
    # run through each col again
    for row in range(len(db)):
        # if the element is in the dictionary get the key of that element and store it in the column array
        if db[row][col] in dict:
            column.append(dict.get(db[row][col]))
    # append everything column to X
    X.append(column)

print(X)

temp1 = []
x = []
# Fixing the X array to be the correct way:
# The X array needs to 4 cols X 10 rows
# The X array right now is the reverse
for i in range(10):
    for j in range(len(X)):
        temp1.append(X[j][i])
    x.append(temp1)
    temp1 = []
X = []
X = x.copy()


#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
Y = [1 if row[-1] == "Yes" else 2 for row in db]


#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()