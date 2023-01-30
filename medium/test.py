from itertools import product

for i, j in product(range(1, 3), range(1, 2)):
    print(i, j)

for i in range(1,3):
    for j in range(1,2):
        print(i,j)