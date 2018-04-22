import numpy as np

a = np.array([1, 3, 4])

b = np.linspace(0, 6, 3)

c = np.random.rand(2, 4)

print("a.dtype: %s " % a.dtype)
print(b)
print(c)
print(c.ravel())
