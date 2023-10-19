import numpy as np 

# Creating array object 
arr = np.array( [[ 1, 2, 3], 
				[ 4, 2, 5]] ) 

# Printing type of arr object 
print("Array is of type: ", type(arr)) 

# Printing array dimensions (axes) 
print("No. of dimensions: ", arr.ndim) 

# Printing shape of array 
print("Shape of array: ", arr.shape) 

# Printing size (total number of elements) of array 
print("Size of array: ", arr.size) 

# Printing type of elements in array 
print("Array stores elements of type: ", arr.dtype) 
""" 
Array is of type:  <class 'numpy.ndarray'>
No. of dimensions:  2
Shape of array:  (2, 3)
Size of array:  6
Array stores elements of type:  int64
 """

# Creating array from list with type float 
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float') 
print ("Array created using passed list:\n", a) 

# Creating array from tuple 
b = np.array((1 , 3, 2)) 
print ("\nArray created using passed tuple:\n", b)
""" 
Array created using passed list:
 [[1. 2. 4.]
 [5. 8. 7.]]

Array created using passed tuple:
 [1 3 2] """

# Creating a 3X4 array with all zeros 
c = np.zeros((3, 4)) 
print ("An array initialized with all zeros:\n", c) 

# Create a constant value array of complex type 
d = np.full((3, 3), 6, dtype = 'complex') 
print ("An array initialized with all 6s."
			"Array type is complex:\n", d) 

# Create an array with random values 
e = np.random.random((2, 2)) 
print ("A random array:\n", e)

""" 
An array initialized with all zeros:
 [[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
An array initialized with all 6s.Array type is complex:
 [[6.+0.j 6.+0.j 6.+0.j]
 [6.+0.j 6.+0.j 6.+0.j]
 [6.+0.j 6.+0.j 6.+0.j]]
A random array:
 [[0.15471821 0.47506745]
 [0.03637972 0.15772238]] """

#  Create a sequence of integers 
# from 0 to 30 with steps of 5 
f = np.arange(0, 30, 5) 
print ("A sequential array with steps of 5:\n", f)
""" 
A sequential array with steps of 5:
[ 0  5 10 15 20 25] """

# Create a sequence of 10 values in range 0 to 5 
g = np.linspace(0, 5, 10) 
print ("A sequential array with 10 values between"
								"0 and 5:\n", g)

""" 
A sequential array with 10 values between0 and 5:
[0.         0.55555556 1.11111111 1.66666667 2.22222222 2.77777778
 3.33333333 3.88888889 4.44444444 5.        ] """

# Reshaping 3X4 array to 2X2X3 array 
arr = np.array([[1, 2, 3, 4], 
				[5, 2, 4, 2], 
				[1, 2, 0, 1]]) 

newarr = arr.reshape(2, 2, 3) 

print ("Original array:\n", arr) 
print("---------------") 
print("Reshaped array1: \n",arr.reshape(4,3))
print("---------------") 
print ("Reshaped array2:\n", newarr)
""" 
Original array:
 [[1 2 3 4]
 [5 2 4 2]
 [1 2 0 1]]
---------------
Reshaped array:
 [[[1 2 3]
  [4 5 2]]
 [[4 2 1]
  [2 0 1]]] """

#  flatten method to get a copy of the array collapsed into one dimension. 
# Flatten array 
arr = np.array([[1, 2, 3], [4, 5, 6]]) 
flat_arr = arr.flatten() 

print ("Original array:\n", arr) 
print ("Fattened array:\n", flat_arr)

""" 
Original array:
 [[1 2 3]
 [4 5 6]]
Fattened array:
 [1 2 3 4 5 6] """
""" 
NumPy Array Indexing
 NumPy array indexing is important for analyzing and manipulating 
                                                the array object
many ways to do array indexing

Slicing: Just like lists in Python, NumPy arrays can be sliced

Integer array indexing: In this method, lists are passed for indexing
                                                    for each dimension

Boolean array indexing  -to pick elements from the array which satisfy some condition. """

# Python program to demonstrate 
# indexing in numpy 

# An exemplar array 
arr = np.array([[-1, 2, 0, 4], 
				[4, -0.5, 6, 0], 
				[2.6, 0, 7, 8], 
				[3, -7, 4, 2.0]]) 

# Slicing array 
temp = arr[:2, ::2] 
print ("Array with first 2 rows and alternate"
					"columns(0 and 2):\n", temp) 

# Integer array indexing example 
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]] 
print ("\nElements at indices (0, 3), (1, 2), (2, 1),"
									"(3, 0):\n", temp) 

# boolean array indexing example 
cond = arr > 0 # cond is a boolean array 
temp = arr[cond] 
print ("\nElements greater than 0:\n", temp) 
print(arr)
print("below is the condition")
print(cond)
""" 
below is the value of cond array which is created
[[False  True False  True]
 [ True False  True False]
 [ True False  True  True]
 [ True False  True  True]]

Array with first 2 rows and alternatecolumns(0 and 2):
 [[-1.  0.]
 [ 4.  6.]]

Elements at indices (0, 3), (1, 2), (2, 1),(3, 0):
 [ 4.  6.  0.  3.]

Elements greater than 0:
 [ 2.   4.   4.   6.   2.6  7.   8.   3.   4.   2. ] """
























































































