import numpy as np

a = np.arange(1, 17).reshape(4, 4)
print(a)
a_rev = a[::-1, :]
print(a_rev)
