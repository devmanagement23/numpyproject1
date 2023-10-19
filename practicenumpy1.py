import numpy as np

arr = np.array([1,2,3])
print("Array with Rank 1 : \n",arr)

arr2 = np.array([9,11,13])
print("Array with Rank 1 : \n",arr)

arr3 = np.array([[1,2,3],[4,5,6]])
print("Array with Rank 2 : \n",arr3)

arr4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array with Rank 2 : \n",arr4)

arr5 = np.array([[[7,8,9],[4,5,6],[1,2,3]],[[7,8,9],[4,5,6],[1,2,3]],[[7,8,9],[4,5,6],[1,2,3]]])
print("Array with Rank 3 : \n",arr5)

print("Array with adding 1 to all : \n",arr + 1)
print("Array with substracting 2 to all : \n",arr - 2)
print("sum of all element of array arr :\n",arr.sum())
print("sum of array aar and arr2 :\n",arr + arr2)

print("type of array arr: ",arr.dtype)

arr11 = np.array([[4,6],[10,11]],dtype =np.float64)
arr12 = np.array([[3,5],[50,60]],dtype= np.float64)

sum = np.add(arr11,arr12)
print("sum of two arrays :",sum)