# run with python 2 or 3

import numpy as np
from sklearn import tree


text = {
    'peel' : [
        'bumpy',
        'smooth'
    ],
    'labels' : [
        'apple',
        'orange'
    ]
}

# [(weight, peel)]
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

prediction = clf.predict([[160, 0]])
print(text['labels'][prediction])


# using normal distribution for the weight
apples = np.random.normal(135, 15, 100)
oranges = np.random.normal(160, 15, 100)
features = [[apple_w, 1] for apple_w in apples] + [[orange_w, 0] for orange_w in oranges]
labels = ([0] * 100) + ([1] * 100)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

prediction = clf.predict([[120, 0]])
print(prediction)
print(text['labels'][prediction])
