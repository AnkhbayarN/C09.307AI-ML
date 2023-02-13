import numpy as np

# a = np.array([1,2,3])
# print(a.shape)
# print(a.ndim)
# print(type(a))
# print('sum:', a.sum())
# print('mean', a.mean())
# print('std', a.std())
# print('max', a.max())

# a = np.array([[1,2,3], [4,5,6]])
# print(a.shape)
# print(a.ndim)

# a = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
# print(a.shape)
# print(a.ndim)

# a = np.array([[[[1,2], [3,4]], [[5,6], [7,8]]], [[[1,2], [3,4]], [[5,6], [7,8]]]])
# print(a.shape)
# print(a.ndim)

# a = np.array([1,2], ndmin = 5)
# print(a.shape)
# print(a.ndim)

# a = np.array([[1,2,3],[4,5,6]])
# print(a)
# b = a.reshape(-1)
# print(b)

d1 = np.array([[1,2], [3,4]])
d2 = np.array([[5,2], [8,10]])

# print('Adding')
# c = d1 + d2
# print(c)

# print('Adding')
# c = d1 * d2
# print(c)

#index
# a = np.array([[1,2,3,4],[5,6,7,8]])
# print(a[0])
# print(a[0][0])
# print(a[1][1:4])
# print(a[0][1:4:2])
# print(a[-2])

# a = np.zeros((5,5))
# print(a)

# a = np.ones((6,5))
# print(a)

# from numpy import random
# a = random.randint(50, size = (5,6))
# print(a)

from numpy import random
a = random.choice([3,5,9], p = [0.5, 0.3, 0.2], size=(20))
print(a)
