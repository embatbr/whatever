# cannot run with python 3 (because of pydot)

import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree


iris = load_iris()

# for i in range(len(iris.target)):
#     print 'Example %d: label %d (%s), features %s' % (i, iris.target[i],
#                                                       iris.target_names[iris.target[i]],
#                                                       iris.data[i])

test_ix = [0, 50, 100] # one from each type

# training data
train_target = np.delete(iris.target, test_ix)
train_data = np.delete(iris.data, test_ix, axis=0)

# testing data
test_target = iris.target[test_ix]
test_data = iris.data[test_ix]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_target)

print test_target
prediction = clf.predict(test_data)
print prediction, iris.target_names[prediction]


from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=iris.feature_names,
                     class_names=iris.target_names, filled=True, rounded=True,
                     impurity=False)

graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf('iris.pdf')

print
print iris.feature_names, iris.target_names
print test_data[0], iris.target_names[test_target[0]]

print
print iris.feature_names, iris.target_names
print test_data[1], iris.target_names[test_target[1]]

print
print iris.feature_names, iris.target_names
print test_data[2], iris.target_names[test_target[2]]