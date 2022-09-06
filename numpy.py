import numpy as np

a = np.mat([[1, 2, 3],
            [3, 5, 6],
            [7, 8, 9]])

b, c = np.linalg.eig(a)
print(b)
print(c)
