from __future__ import print_function
import numpy as np
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(7)
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
print("Labels:", np.unique(iris_y))

# split train and test
X_Train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=130)
print("Train size: ", X_Train.shape[0], ", Test Size: ", X_test.shape[0])

model = neighbors.KNeighborsClassifier(n_neighbors=5, p = 2, weights="distance")
model.fit(X_Train, y_train)
y_pred = model.predict(X_test)
print("y_pred: ", y_pred) 
print("Accuracy of 1NN: ", 100 * accuracy_score(y_test, y_pred))

