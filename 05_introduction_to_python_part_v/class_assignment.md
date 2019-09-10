# Class assignment 

Write a module `vec3.py` that contains class Vector that represents 3D vectors with x, y, and z coordinates. Fill in all attributes / methods below as well as all operations in your assignment file. 

There should be two files `vec3.py` and `assignment.py`

```python

class Vector3:
	"""
	A class that represents 3D vectors with x, y and z coordinates
	"""

	def __init__(self, x, y, z):
		# set internal x, y, and z attributes
		pass
	
	def __str__(self):
		# prints out the value of x, y and z when using str() function or
		# print 
		# returns string 
	
	def __add__(self, other):
		# adds two vectors together
		# returns a Vector3 object that is the sum of the two vectors 
		pass
		
	def __div__(self, other):
		# return vector divided by other. Each element is divided by the same
		# value 
		# returns a Vector3 object 
		
	def __mult__(self, other):
		# return vector multiplied by other. Each element is multiplied by the same value
		# returns a Vector3 object
		
	def __sub__(self, other):
		# substracts the other vector from the current vector 
		# returns a Vector3 object that is the result of this subtraction
		
	def distance(self, other):
		# calculates the distance betwen current vector and other
		# distance is math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
		# return the distance 
		
	def dot(self, other):
		# calculate to dot product between current vector and other
		# dot is x1*x2 + y1*y2 + z1*z2
		
	def negated(self):
		# returns negated vector puts a - sign infront of x, y, and z 
		# returns a Vector3 object
		
	def magnitude(self):
		# returns the magnitude of the vector
		# math.sqrt(x*x + y*y + z*z) 
		
	def normalize(self):
		# normalize vector by dividing each element by the magnitude
		# returns nothing 
	

```

In your assignment python file  

```python 

import vec3 

# uncomment as you get functionality working 
# origin = vec3.Vector3(0.0, 0.0, 0.0)
# v1 = vec3.Vector3(1.0, 2.0, 3.0)
# v2 = vec3.Vector3(10.0, 10.0, 10.0)
# v_sum = v1 + v2 
# v_sub = v1 - v2 
# v_mult = v1 * 3
# v_div = v1 / 3.0
# print(v_sum.distance(origin))
# print(v_sub.negated())
# v_mult.normalize()
# print(v_mult)
# print(v1.dot(v2))



```




