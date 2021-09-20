# Decision Tree
##### This algorithm was developed for the first assignment of Introduction to Machine Learning class
---
### Description:
###### This algorithm takes in input data with binary class labels, and processes the data in order to train a decision tree 
to determine if a patient needs corrective lenses with their given condition. The algorithm is a decision tree with entropy as its
way of classifying which attribute to select an attribute for any given level of the tree. at the end a visual representation of the
graph is displayed.

---
### Data Set:
###### as mentioned the data set consists of conditions for each patient. 
The attributes are:
* Age
* Spectacle Prescription
* Astigmatism
* Tear Production Rate

the class attribute is the recommendations regarding Lenses and it is a binary class.
---
### How:
###### The algorithm constructs a tree with the best attribute chosen as root node. The best node is decided using the entropy/gain method. This uses the following formula to calculate entropy:
### Entropy(s) = -p<sub>+</sub> log<sub>2</sub><sup>P<sub>+</sub></sup> -p<sub>-</sub> log<sub>2</sub><sup>P<sub>-</sub></sup>
###### to calculate gain:
---
### What did I learn?
###### 
---
### Using: 
* Python
* sklearn
* matplotlib
* CSV
