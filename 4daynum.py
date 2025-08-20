import numpy as np

arr = np.array([41, 42, 43, 44])
filterArr= arr>42

newArr= arr[filterArr]
print(filterArr)
print(newArr)