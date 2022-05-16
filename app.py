import numpy as np

#print(np.__version__)
x = np.zeros(10)
#print(x)
#print(x.size * x.itemsize)
#print(np.info())

#x[4] = 1
#print(x)

#x = np.arange(10,50)
#print(x)

#x=np.arange(0,10)
#print(x[::-1])

#x = np.arange(0,9).reshape(3,3)
#print(x)

#x = np.array([1, 2, 0,0,4,0])
#print(np.nonzero(x))

#x = np.eye(3,3)
#print(x)

#arr = np.random.random(3)

#arr = np.random.random(10)
#arr.max()
#print(arr.mean())

#matrix = np.ones((5,5))
#matrix[1:-1,1:-1] = 0
#print(matrix)

#matrix = np.ones((5,5))
#matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values=0)
#print(matrix)


#print(0 * np.nan)
#print(np.nan == np.nan)
#print(np.inf > np.nan)
#print(np.nan - np.nan)
#print(np.nan in set([np.nan]))
#print(0.3 == 3 * 0.1)

#x = np.arange(0,9).reshape(3,3)
#print(np.diag(x))

x = np.ones((3,3))
x = np.zeros((8,8))
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)