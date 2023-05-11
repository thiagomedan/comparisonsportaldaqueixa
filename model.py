from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import pickle

iris = load_iris()
X = iris["data"]
y = iris["target"]

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X,y)

pickle.dump(model, open("knnC.p","wb"))