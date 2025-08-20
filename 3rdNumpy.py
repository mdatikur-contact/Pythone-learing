import numpy as np

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for idx, x in np.ndenumerate(arr):
#     print(idx, x)
ar1 =np.array([1,2,3])
ar2 =np.array([4,5,6])
ajoin= np.hstack((ar1, ar2))
print(np.array_split(ajoin, 3) )
print(ajoin)