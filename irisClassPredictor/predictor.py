"""
@author: Sourabh Sinha
This File loads the Iris dataset and fits a RamdomForest classifier
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

#load iris dataset
iris = load_iris()
X = iris.data
y = iris.target

#Split data in train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.5)

#Build model
clf = RandomForestClassifier(n_estimators=10)

# Train the classifier
clf.fit(X_train, y_train)

#Predictions
predicted = clf.predict(X_test)

#Check accuracy
print(accuracy_score(predicted, y_test))

with open("./iris_rf.pkl", "wb") as model_pkl:
    pickle.dump(clf, model_pkl)

