import vec3

#uncomment as you get functionality working
origin = vec3.Vector3(0.0, 0.0, 0.0)
v1 = vec3.Vector3(1.0, 2.0, 3.0)
v2 = vec3.Vector3(10.0, 10.0, 10.0)
v_sum = v1 + v2
v_sub = v1 - v2
v_mult = v1 * 3
v_div = v1 / 3.0
print(v_sum.distance(origin))
print(v_sub.negated())
v_mult.normalize()
print(v_mult)
print(v1.dot(v2))