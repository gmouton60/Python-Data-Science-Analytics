# -*- coding: utf-8 -*-
"""GMlab5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DuJxiOvqTSQaUH4U-rBiIMP481MioK86
"""

# Commented out IPython magic to ensure Python compatibility.
# %pylab inline

"""## Implement the function to calculate gini index given the fraction of two classes"""

import numpy as np

def gini(p1, p2):
    return 1-p1*p1 - p2*p2
   

x = np.arange(0.0, 1.0, 0.01)
plt.plot(x, gini(x, 1-x))
plt.ylim([0, 1.1])
plt.xlabel('p(i=1)')
plt.axhline(y=0.5, linewidth=1, color='k', linestyle='--')
plt.ylabel('Gini Impurity')
plt.show()

"""-----------------------------------------------------------------------

## Decision Tree
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)
print(np.unique(y))

help(DecisionTreeClassifier)

"""Task 1
---
Build a decision tree model using the training data (X_train, y_train). Use the model to make prediction on the testing data (X_test). Calculate the *accuracy* of the prediction comparing to the treu class label (y_test).
"""

tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)
p = tree.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, p))

print(np.sum(y_test == p)/len(p))

"""Task 2
---
Using GridSearchCV, do a search to find the values for 'min_samples_leaf' (1, 5, 10) and 'max_depth' (2, 3, 4) that give the best prediction accuracy. Print the grid scores and the best values.
"""

from sklearn.model_selection import GridSearchCV
help(GridSearchCV)

tree_clf = DecisionTreeClassifier()
tree_search_params = {'min_samples_leaf':[1, 5, 10],
                     'max_depth':[2, 3, 4]}
tree_search = GridSearchCV(tree_clf, tree_search_params, cv=5, verbose=0)
tree_search.fit(X, y)

print(tree_search.best_score_)
print(tree_search.best_params_)

import pandas as pd
score = pd.DataFrame(tree_search.cv_results_)
score[score.columns[6:13]]

"""-----------------------------------------------------------------------"""