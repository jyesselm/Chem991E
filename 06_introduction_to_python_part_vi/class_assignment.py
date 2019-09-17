import shape_factory 

sf = shape_factory.ShapeFactory()
shapes = []
for i in range(3):
	shapes.append(sf.get_shape("circle"))
	shapes.append(sf.get_shape("square"))
	shapes.append(sf.get_shape("rectangle"))

for s in shapes:
	print(s.shape_type(), s.area())

shapes_2 = []
for i in range(10):
	shapes_2.append(sf.get_random_shape())

print("random shapes")
for s in shapes_2:
	print(s.shape_type(), s.area())
