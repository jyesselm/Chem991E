# Class assignment 

Write a module `shape_factory.py` that contains four functions 

```python
import random

class Shape(object):
	def __init__(self):
		pass
		
	def shape_type():
		# return a string of what type of shape this is "circle", "square"
		pass
		
	def area():
		# returns area 
		pass
		
class Circle(Shape):
	def __init__(self, radius):
		pass
	
	def area():
		pass
		
class Square(Shape):
	def __init__(self, length):
		pass
		
	def area():
		pass
		
class Rectangle(Shape):
	def __init__(self, width, height):
		pass
		
	def area():
		pass
		
		
class ShapeFactory(object):
	def get_shape(name):
		if name == "circle":
			return Circle(random.randint(1, 10))
		
		elif name == "square":
			# return square with random length
			pass
			
		elif name == "rectangle":
			# return recrangle with random width and length
			pass
			
	def get_random_shape():
		# returns a random shape with random properties 
		pass

```

In your assignment python file  

```python 

import shape_factory 

#sf = shape_factory.ShapeFactory()
#shapes = []
#for i in range(3):
#	shapes.append(sf.get_shape("circle"))
#	shapes.append(sf.get_shape("square"))
#	shapes.append(sf.get_shape("rectangle"))

#for s in shapes:
#	print(s.shape_type(), s.area())

#shapes_2 = []
#for i in range(10):
#	shapes_2.append(sf.get_random_shape())

#print("random shapes")
#for s in shapes_2:
#	print(s.shape_type(), s.area())
```




