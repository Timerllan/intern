import unittest
from shape import Circle, Triangle, compute_area


class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(compute_area(circle), 78.53981633974483)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(compute_area(triangle), 6.0)

    def test_is_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())
        triangle2 = Triangle(2, 2, 3)
        self.assertFalse(triangle2.is_right_triangle())


if __name__ == '__main__':
    unittest.main()
