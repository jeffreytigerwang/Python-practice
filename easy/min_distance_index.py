import numpy as np
from scipy.spatial import distance
from scipy.spatial.distance import cdist

s1 = np.array([(0,0,1), (0,1,1), (1,0,2), (1,1,1)])
s2 = np.array([(3,2,0), (0,1,1),(0,0,1)])

values = cdist(s1,s2).min(axis=1)

values2 = np.argmin(values)
print(values)
print(values2)
# array([3.60555128, 3.16227766, 2.82842712, 2.23606798])


values1 = np.argmin(cdist(s1,s2),1)

print(values1)

