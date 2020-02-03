# Machine Learning in Python
# What is ML? Using a computer to generate knowledge from data, like image recognition.
# Modules used: scipy (installs scipy and numpy too), scikit-learn, and ipython
# python3 -m pip install scipy
# python3 -m pip install scikit-learn
# python3 -m pip install ipython
# python3 -m pip install "ipython[notebook]" - for something called jupyter notebook lol
# python3 -m ipykernel install --user
# since that didn't work, try: brew install jupyter
# I guess we're abandoning this IDE
# to open Jupyter Notebook, in terminal type "jupyter notebook".

# The Iris Dataset:
# In 1936, biologist Ronald Fisher collected 150 samples of Iris flowers, divided into 50 samples of three different species of Iris flowers
# From each of them, he took measurements of the petal and the sepal
# We're going to use the 150 samples to train the computer; we're going to apply statistical models to make our computer
# be able to identify the species of an Iris flower by its measurements

from sklearn.datasets import load_iris
iris = load_iris()
print(iris)
print("")
print(iris.data)
print("")
print(iris.target)
print("")
print(iris.target_names)

# A way that a computer can learn from data is by using statistical models. One model we'll use is the KNN model.
# KNN - K nearest neighbours. Every time we work with this model we have to define a value for K to find that many nearest neighbours
# Using its nearest neighbours, it can accurately predict values; re: the example of green and blue petals and finding the next nearest neighbour

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)     # using 1 as number of neighbours. not sure if accurate, but we have tools to help determine
X = iris.data                                   # data
Y = iris.target                                 # target
knn.fit(X,Y)                                    # in knn.predict(), need to pass an observation; a list of 4 values as denoted in the iris set
print(knn.predict([[5.1, 3.5, 1.4, 0.2]]))      # we expect species 0 since we just copied some data from the above table lol
print(knn.predict([[6.3, 2.5, 5.0, 1.9]]))      # we expect species 2

# how do we make sure that our computer is actually thinking intelligently and not just doing table lookup?
# we can divide our table of 150 into two groups, train it on group one, test it on group 2.