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
Array is of type:  <class 'numpy.ndarray'>           /  type(arr)
No. of dimensions:  2								/ arr.ndim
Shape of array:  (2, 3)								/ arr.shape
Size of array:  6									/ arr.size
Array stores elements of type:  int64				/ arr.dtype
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
cond = arr > 0 # cond is a boolean array ,new array cond created
temp = arr[cond]  # a new array is created

print("below is the condition")
print(cond)
print ("\nElements greater than 0:\n", temp) 
print(arr)

""" 


Array with first 2 rows and alternatecolumns(0 and 2):
 [[-1.  0.]
 [ 4.  6.]]

Elements at indices (0, 3), (1, 2), (2, 1),(3, 0):
 [ 4.  6.  0.  3.]
 
 below is the value of cond array which is created
 below is the condition

[[False  True False  True]
 [ True False  True False]
 [ True False  True  True]
 [ True False  True  True]]

Elements greater than 0:
 [ 2.   4.   4.   6.   2.6  7.   8.   3.   4.   2. ] """

# Python program to demonstrate 
# basic operations on single array 
import numpy as np 

a = np.array([1, 2, 5, 3]) 

# add 1 to every element 
print ("Adding 1 to every element:", a+1) 

# subtract 3 from each element 
print ("Subtracting 3 from each element:", a-3) 

# multiply each element by 10 
print ("Multiplying each element by 10:", a*10) 

# square each element 
print ("Squaring each element:", a**2) 

# modify existing array 
a *= 2
print ("Doubled each element of original array:", a) 

# transpose of array 
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]]) 

print ("\nOriginal array:\n", a) 
print ("Transpose of array:\n", a.T) 
""" 
Adding 1 to every element: [2 3 6 4]
Subtracting 3 from each element: [-2 -1  2  0]
Multiplying each element by 10: [10 20 50 30]
Squaring each element: [ 1  4 25  9]
Doubled each element of original array: [ 2  4 10  6]

Original array:
 [[1 2 3]
  [3 4 5]
  [9 6 0]]
Transpose of array:
 [[1 3 9]
  [2 4 6]
  [3 5 0]]
 """

# Python program to demonstrate 
# unary operators in numpy 
import numpy as np 

arr = np.array([[1, 5, 6], 
				[4, 7, 2], 
				[3, 1, 9]]) 

# maximum element of array 
print ("Largest element is:", arr.max()) 
print ("Row-wise maximum elements:", 
					arr.max(axis = 1)) 

# minimum element of array 
print ("Column-wise minimum elements:", 
						arr.min(axis = 0)) 

# sum of array elements 
print ("Sum of all array elements:", 
							arr.sum()) 

# cumulative sum along each row 
print ("Cumulative sum along each row:\n", 
						arr.cumsum(axis = 1)) 
""" 
Largest element is: 9
Row-wise maximum elements: [6 7 9]
Column-wise minimum elements: [1 1 2]
Sum of all array elements: 38
Cumulative sum along each row:
[[ 1  6 12]
 [ 4 11 13]
 [ 3  4 13]] """
#-------------------OPERATOR OVERLOADING VS FUNCTIONS------------
# Python program to demonstrate 
# binary operators in Numpy 
import numpy as np 

a = np.array([[1, 2], 
			[3, 4]]) 
b = np.array([[4, 3], 
			[2, 1]]) 

# add arrays 
print ("Array sum:\n", a + b) 

# multiply arrays (elementwise multiplication) 
print ("Array multiplication:\n", a*b) 

# matrix multiplication 
print ("Matrix multiplication:\n", a.dot(b)) 

""" 
Array sum:
[[5 5]
 [5 5]]
Array multiplication:
[[4 6]
 [6 4]]
Matrix multiplication:
[[ 8  5]
 [20 13]] """

# Python program to demonstrate 
# universal functions in numpy 
import numpy as np 

# create an array of sine values 
a = np.array([0, np.pi/2, np.pi]) 
print ("Sine values of array elements:", np.sin(a)) 

# exponential values 
a = np.array([0, 1, 2, 3]) 
print ("Exponent of array elements:", np.exp(a)) 

# square root of array values 
print ("Square root of array elements:", np.sqrt(a)) 
""" 
Sine values of array elements: 
			[  0.00000000e+00   1.00000000e+00   1.22464680e-16]

Exponent of array elements: 
			[  1.           2.71828183   7.3890561   20.08553692]

Square root of array elements:
			[ 0.          1.          1.41421356  1.73205081] """


# Python program to demonstrate sorting in numpy 

a = np.array([[1, 4, 2], 
				[3, 4, 6], 
			[0, -1, 5]]) 

# sorted array 
print ("Array elements in sorted order:\n", 
					np.sort(a, axis = None)) 

# sort array row-wise 
print ("Row-wise sorted array:\n", 
				np.sort(a, axis = 1)) 

# specify sort algorithm 
print ("Column wise sort by applying merge-sort:\n", 
			np.sort(a, axis = 0, kind = 'mergesort')) 

# Example to show sorting of structured array 
# set alias names for dtypes 
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)] 

# Values to be put in array 
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7), 
		('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)] 
			
# Creating array 
arr = np.array(values, dtype = dtypes) 
print ("\nArray sorted by names:\n", 
			np.sort(arr, order = 'name')) 
			
print ("Array sorted by graduation year and then cgpa:\n", 
				np.sort(arr, order = ['grad_year', 'cgpa'])) 
""" 
Array elements in sorted order, when axis = none :
[-1  0  1  2  3  4  4  5  6]
Row-wise sorted array:
[[ 1  2  4]
 [ 3  4  6]
 [-1  0  5]]
Column wise sort by applying merge-sort:
[[ 0 -1  2]
 [ 1  4  5]
 [ 3  4  6]]

Array sorted by names:
[('Aakash', 2009, 9.0) ('Ajay', 2008, 8.7) ('Hrithik', 2009, 8.5)
 ('Pankaj', 2008, 7.9)]
Array sorted by graduation year and then cgpa:
[('Pankaj', 2008, 7.9) ('Ajay', 2008, 8.7) ('Hrithik', 2009, 8.5)
 ('Aakash', 2009, 9.0)] """

#--------------------------------------------------------
#Create NumPy Array from a List

li = [1,2,3,4]
numpyArr = np.array(li)

#or

numpyArr = np.array([1,2,3,4])

# in above The list is passed to the array() method which returns
#  a NumPy array with the same elements
#-------------------------

li = [1, 2, 3, 4]
numpyArr = np.array(li)

print("li =", li, "and type(li) =", type(li))
print("numpyArr =", numpyArr, "and type(numpyArr) =", type(numpyArr))
""" 
li = [1, 2, 3, 4] and type(li) = <class 'list'>
numpyArr = [1 2 3 4] and type(numpyArr) = <class 'numpy.ndarray'> """

#-----------------
#Create NumPy Array from a Tuple

tup = (1,2,3,4)
numpyArr = np.array(tup)
#OR
numpyArr = np.array((1,2,3,4))

print("tup =", tup, "and type(tup) =", type(tup))
print("numpyArr =", numpyArr, "and type(numpyArr) =", type(numpyArr))
""" 
tup = (1, 2, 3, 4) and type(tup) = <class 'tuple'>
numpyArr = [1 2 3 4] and type(numpyArr) = <class 'numpy.ndarray'> """

# creating list 
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]
 
# creating numpy array
sample_array = np.array([list_1,
                         list_2,
                         list_3])
 
print("Numpy array :")
print(sample_array)
 
# print shape of the array
print("Shape of the array :",
      sample_array.shape)
""" 
Numpy array : 
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
Shape of the array :  (3, 4) """

#---------------------
# numpy.fromiter(): The fromiter() function create a new one-dimensional array 
# from an iterable object.

# iterable
iterable = (a*a for a in range(8))
print("thi si me :",iterable)

for x in iterable:
  print(x)

arr2 = np.fromiter(iterable, float)

print("fromiter() array :",arr2)
""" 
thi si me : <generator object <genexpr> at 0x0000026E50075D20>
fromiter() array :  [ 0.  1.  4.  9. 16. 25. 36. 49.] 
 """

var = "Geekforgeeks"

arr = np.fromiter(var, dtype = 'U2')

print("fromiter() array :",	arr)

#fromiter() array : ['G' 'e' 'e' 'k' 'f' 'o' 'r' 'g' 'e' 'e' 'k' 's']
#-----------------

#Syntax: numpy.arange(start,stop,step,dtype=None)

np.arange(1, 20 , 2, dtype = np.float32)

#array([ 1.,  3.,  5.,  7.,  9., 11., 13., 15., 17., 19.])

#Syntax: numpy.ones(shape, dtype=None, order=’C’)
np.ones([4, 3],dtype = np.int32, order = 'f')
""" 
array([[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]) """

np.zeros([4, 3],dtype = np.int32, order = 'f')
""" 
array([[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]) """






















































































