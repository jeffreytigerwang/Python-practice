import numpy as np


def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


def softmax(x):
    f_x = np.exp(x) / np.sum(np.exp(x))
    return f_x


a = np.array([[5, -2, 4, 0],
             [5, -1, 6, 2],
              [10,-3,-2,5],
             [0, 1, 4, -1],
             [-3, 4, 9, 3]])

# print(NormalizeData(a))

a_pr = np.copy(NormalizeData((a)))
for i in range(5):
    a_pr[i] = softmax(a_pr[i])

print(a_pr)
