""" Name - Akshay Lavhagale
    HW 01: Testing triangle classification
    The function returns a string that specifies whether the triangle is scalene, isosceles, or equilateral,
    and whether it is a right triangle as well. """

import unittest
from HW_01 import classify_triangle, run_classify_triangle


class TestTriangles(unittest.TestCase):
    # This class will test all the triangle specification and classify them as per their characteristics.
    def test_input(self):
        # This function will check whether all the data points are present in correct format or not
        with self.assertRaises(ValueError):
            classify_triangle("Akshay", 1, 2)
            classify_triangle("a", "b", "c")
            classify_triangle("A", "B", "C")

    def test_equilateral(self):
        # This function will tell us whether the triangle is equilateral triangle or not
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 is an equilateral')
        self.assertNotEqual(classify_triangle(3, 3, 12), 'Equilateral', '3,3,12 is an isosceles')
        self.assertEqual(classify_triangle(15.5, 15.5, 15.5), 'Equilateral', '15.5, 15.5, 15.5 is an equilateral')

    def test_isosceles(self):
        # This function will tell us whether the triangle is isosceles triangle or not
        self.assertEqual(classify_triangle(2, 2, 3), 'Isosceles', '2, 2, 3 is an isosceles triangle')
        self.assertEqual(classify_triangle(12, 13, 12), 'Isosceles', '12, 13, 12 is an isosceles triangle')
        self.assertEqual(classify_triangle(10, 10, 8), 'Isosceles', '10, 10, 8 is an isosceles triangle')
        self.assertNotEqual(classify_triangle(10, 10, 10), 'Isosceles', '10, 10, 10 should be Equilateral')

    def test_scalene(self):
        # This function will tell us whether the triangle is scalene triangle or not
        self.assertEqual(classify_triangle(10, 20, 12), 'Scalene', '10, 20, 12 is a scalene triangle')
        self.assertNotEqual(classify_triangle(10, 10, 3), 'Scalene', '10, 10, 3 is an isosceles triangle')

    def test_isosceles_right(self):
        pass
        # This function will tell us whether the triangle is isosceles and right triangle or not
        # self.assertEqual(classify_triangle(2, 2, 2.828), 'Isosceles and Right Triangle',
        # '2, 2, 2.828 is an isosceles and right triangle')

    def test_scalene_right(self):
        # This function will tell us whether the triangle is scalene and right triangle or not
        self.assertEqual(classify_triangle(3, 4, 5), 'Right and Scalene Triangle',
                         '3, 4, 5 is a scalene and right Triangle')

    def test_not_triangle(self):
        # This function will tell us whether this is triangle or not
        # self.assertEqual(classify_triangle(1, 1, 3), 'This is not a triangle', '1, 1, 3 is not a triangle')
        self.assertEqual(classify_triangle(15.5, 15.5, -15.5), 'This is not a triangle',
                         '15.5, 15.5, -15.5 is not a triangle')
        self.assertEqual(classify_triangle(0, 0, 0), 'This is not a triangle', '0, 0, 0 is not a triangle')


if __name__ == '__main__':
    run_classify_triangle(5, 6, 7)
    run_classify_triangle(9, 9, 9)
    run_classify_triangle(8, 15, 17)
    run_classify_triangle(2, 2, 4)
    unittest.main(exit=False, verbosity=2)
