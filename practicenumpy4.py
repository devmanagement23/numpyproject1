
import numpy as np
 
var = "Geekforgeeks"
 
arr = np.fromiter(var, dtype = 'U2')
 
print("fromiter() array :",
      arr)