import unittest

import vec3 

class Vec3Unittest(unittest.TestCase):
    
    def test_creation(self):
        # TODO check to make sure x y and z are set correctly
        # i.e.
        # v = vec3.Vector3(0.0, 1.0, 2.0)
        # does v.x == 0.0?
        pass

    def test_vec3_only_accepts_nums(self):
        # TODO make sure the Vector3 only takes numbers as x, y and z
        # i.e.
        # v = vec3.Vector3("test", "test", "test")
        # this should return an error, check for that
        pass

    def test_add(self):
        # TODO make sure v1 + v2 works properly
        # just check result
        # i.e.
        # v1 = vec3.Vector3(0.0, 1.0, 2.0)
        # v2 = vec3.Vector3(0.0, 1.0, 2.0)
        # v3 = v1 + v2
        # is v3.z == 4.0?
        pass


    def test_sub(self):
        # TODO make sure v1 - v2 works properly, see test_add example
        pass

    def test_mul(self):
        # TODO make sure v1 * 2 works properly, see test_add example
        pass

    def test_div(self):
        # TODO make sure v1 / 2 works properly, see test_add example
        pass

    def test_distance(self):
        # TODO test to make sure distance works
        # i.e.
        # vec1 = vec3.Vector3(0.0, 0.0, 0.0)
        # vec2 = vec3.Vector3(0.0, 0.0, 9.0)
        # vec1.distance(vec2) == 3 ?
        pass

    def test_dot_product(self):
        # TODO test to make sure dot product works
        pass


    def test_negate(self):
        # TODO test to make sure that negated works
        pass


    def test_magnitude(self):
        # TODO make sure magnitude works
        pass


    def test_normalize(self):
        # TODO make sure normaliz works
        pass


unittest.main()
