# -*- coding: utf-8 -*-
"""task 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ys4NYUXFySLVfKzUO7PYChVqBomkguCr

**Data science internship**

**Batch=August 2023**

**Task- Prediction using decision tree algorithm(level-intermediate)**

Pranali Dattaram Tatkare
"""

from numpy.random.mtrand import standard_cauchy
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error,r2_score,accuracy_score
import matplotlib.pyplot  as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

data=load_iris()
X=data.data
y=data.target

X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2,random_state=42)

clf=DecisionTreeClassifier()
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)
print(y_pred)

accuracy=accuracy_score(y_pred,y_test)
print('Test accuracy',accuracy)

plt.scatter(y_pred,y_test,color='red')
plt.plot(y_pred,clf.predict(X_test),color='blue')
plt.title('Decision tree',size=14,color='blue')