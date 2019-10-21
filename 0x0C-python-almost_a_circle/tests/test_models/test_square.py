#!/usr/bin/python3
""" Importing modules """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test Class. A testcase is created by subclassing unittest.TestCase. """
    def test_nb_objects(self):
        """ Tests __nb_objects if created an instance """
        obj1 = Square(1, 2, 3, 4)
        self.assertIsInstance(obj1, Square)

    def test_size_negative(self):
        """ Tests if size is negative """
        with self.assertRaises(ValueError) as width_error:
            obj1 = Square(-1, 1)
        self.assertEqual('width must be > 0', str(width_error.exception))

    def test_size_zero(self):
        """ Tests if size is zero """
        with self.assertRaises(ValueError) as width_error:
            obj1 = Square(0, 1)
        self.assertEqual('width must be > 0', str(width_error.exception))

    def test_size_string(self):
        """ Tests if size is a string """
        with self.assertRaises(TypeError) as width_error:
            obj1 = Square("hello", 1)
        self.assertEqual('width must be an integer', str(width_error.exception))

    def test_size_tuple(self):
        """ Tests if size is a tuple """
        with self.assertRaises(TypeError) as width_error:
            obj1 = Square((1, 2, 3, 4), 1)
        self.assertEqual('width must be an integer', str(width_error.exception))

    def test_size_list(self):
        """ Tests if size is a list """
        with self.assertRaises(TypeError) as width_error:
            obj1 = Square([1, 2, 3, 4], 1)
        self.assertEqual('width must be an integer', str(width_error.exception))

    def test_size_float(self):
        """ Tests if size is float """
        with self.assertRaises(TypeError) as width_error:
            obj1 = Square(2.4, 1)
        self.assertEqual('width must be an integer', str(width_error.exception))

    def test_size_set(self):
        """ Tests if size is a set """
        with self.assertRaises(TypeError) as width_error:
            obj1 = Square({1, 2, 3, 4, 5}, 1)
        self.assertEqual('width must be an integer', str(width_error.exception))

    def test_size_long(self):
        """ Tests if arg long int, eventhough it doesn't exist in Python3 """
        obj1 = Square(1000000)

    def test_x_negative(self):
        """ Tests if x is negative """
        with self.assertRaises(ValueError) as x_error:
            obj1 = Square(1, -4)
        self.assertEqual('x must be >= 0',
                         str(x_error.exception))
    def test_x_zero(self):
        """ Tests if x is zero """
        obj1 = Square(1, 0)

    def test_x_string(self):
        """ Tests if x is a string """
        with self.assertRaises(TypeError) as x_error:
            obj1 = Square(1, 'Python')
        self.assertEqual('x must be an integer',
                         str(x_error.exception))

    def test_x_tuple(self):
        """ Tests if x is a tuple """
        with self.assertRaises(TypeError) as x_error:
            obj1 = Square(1, (1, 2, 3))
        self.assertEqual('x must be an integer',
                         str(x_error.exception))

    def test_x_list(self):
        """ Tests if x is a list """
        with self.assertRaises(TypeError) as x_error:
            obj1 = Square(1, [1, 2, 3, 4])
        self.assertEqual('x must be an integer',
                         str(x_error.exception))

    def test_x_float(self):
        """ Tests if x is a float """
        with self.assertRaises(TypeError) as x_error:
            obj1 = Square(1, 3.14159)
        self.assertEqual('x must be an integer',
                         str(x_error.exception))

    def test_x_set(self):
        """ Tests if x is a set """
        with self.assertRaises(TypeError) as x_error:
            obj1 = Square(1, (1, 2, 3, 4))
        self.assertEqual('x must be an integer',
                         str(x_error.exception))

    def test_x_long(self):
        """ Tests if x is a long int, which in Python3 is the same as int """
        obj1 = Square(1, 10000000000000)

    def test_y_negative(self):
        """ Tests if y is negative """
        with self.assertRaises(ValueError) as y_error:
            obj1 = Square(1, 2, -1)
        self.assertEqual('y must be >= 0',
                         str(y_error.exception))
    def test_y_zero(self):
        """ Tests if y is zero """
        obj1 = Square(1, 2, 0)

    def test_y_string(self):
        """ Tests if y is a string """
        with self.assertRaises(TypeError) as y_error:
            obj1 = Square(1, 2, 'hello')
        self.assertEqual('y must be an integer',
                         str(y_error.exception))

    def test_y_tuple(self):
        """ Tests if y is a tuple """
        with self.assertRaises(TypeError) as y_error:
            obj1 = Square(1, 2, (1, 2, 3))
        self.assertEqual('y must be an integer',
                         str(y_error.exception))

    def test_y_list(self):
        """ Tests if y is a list """
        with self.assertRaises(TypeError) as y_error:
            obj1 = Square(1, 2, [1, 2, 3, 4])
        self.assertEqual('y must be an integer',
                         str(y_error.exception))

    def test_y_float(self):
        """ Tests if y is a float """
        with self.assertRaises(TypeError) as y_error:
            obj1 = Square(1, 2, 3.14159)
        self.assertEqual('y must be an integer',
                         str(y_error.exception))

    def test_y_set(self):
        """ Tests if y is a set """
        with self.assertRaises(TypeError) as y_error:
            obj1 = Square(1, 2, (1, 2, 3, 4))
        self.assertEqual('y must be an integer',
                         str(y_error.exception))

    def test_y_long(self):
        """ Tests if y is a long int, which in Python3 is the same as int """
        obj1 = Square(1, 2, 10000000000000)


    def test_correct(self):
        """ Tests correct input """
        obj1 = Square(1, 1, 5, 5)

    def test_no_args(self):
        """ Tests if no argument is passed """
        with self.assertRaises(TypeError):
            obj1 = Square()

    def test_more_args(self):
        """ Tests if more number of arguments are passed """
        with self.assertRaises(TypeError):
            obj1 = Square(5, 4, 3, 2, 1, 0)

    def test_none(self):
        """ Tests if None is passed as an argument """
        with self.assertRaises(TypeError):
            obj1 = Square(None)

    def test_area(self):
        """ Tests area method """
        obj1 = Square(6, 6, 6, 6)

        self.assertEqual(obj1.area(), 36)

    def test_update(self):
        """ Tests if update method works """
        obj1 = Square(1, 2, 3, 4)
        obj1.update(size=4, x=3, y=2, id=1)

    def test_one_arg(self):
        """ Tests if only one argument is passed """
        obj1 = Square(1)

if __name__ == '__main__':
    unittest.main()
