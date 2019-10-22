#!/usr/bin/python3
""" Importing unittest module in order to test expected results """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Test class. A test case is created by subclassing unittest.TestCase """

    def test_id_int(self):
        """ Testing if id is corrected when inserted """
        obj1 = Base(50)
        self.assertEqual(obj1.id, 50)

    def test_nb_objects(self):
        """ Tests if __nb_objects increases if object is created """
        obj1 = Base(50)
        self.assertIsInstance(obj1, Base)

    def test_id_zero(self):
        """ Tests if id is 0 """
        obj1 = Base(0)
        self.assertEqual(obj1.id, 0)

    def test_id_long(self):
        """
        Tests if id is a long int. Just testing a
        long integer as long int doesn't exist in Python3
        """
        obj1 = Base(1000000)
        self.assertEqual(obj1.id, 1000000)

    def test_id_string(self):
        """ Tests if id is a string """
        obj1 = Base('Hello')
        self.assertEqual(obj1.id, 'Hello')

    def test_id_float(self):
        """ Tests if id is a float """
        obj1 = Base(3.0)
        self.assertEqual(obj1.id, 3.0)

    def test_id_negative(self):
        """ Tests if id is a int negative """
        obj1 = Base(-1)
        self.assertEqual(obj1.id, -1)

    def test_to_json_string_none(self):
        """ Tests if list_dicitionaries is None """
        obj1 = Base.to_json_string(None)
        self.assertEqual(obj1, '[]')

    def test_to_json_string_not_list(self):
        """ Tests if list_dictionaries is not a list """
        with self.assertRaises(TypeError) as list_error:
            Base.to_json_string("Hello")
        self.assertEqual('list_dictionaries must be a list',
                         str(list_error.exception))

    def test_to_json_string_not_list_dict(self):
        """ Tests if list_dictionaries is a list of not dictionaries """
        with self.assertRaises(TypeError) as dict_error:
            Base.to_json_string(['Hello', 'How', 'are', 'you'])
        self.assertEqual('Must be a list of dictionaries',
                         str(dict_error.exception))

    def test_to_json_string_correct(self):
        """ Tests correct input """
        list_dict = {'id': 1, 'height': 5, 'width': 5}
        json_string = Base.to_json_string([list_dict])
        self.assertTrue(isinstance(list_dict, dict))
        self.assertEqual(json_string, '[{"id": 1, "height": 5, "width": 5}]')
        self.assertTrue(isinstance(json_string, str))

    def test_save_to_file_not_list(self):
        """ Tests if list_objs is not a list """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        with self.assertRaises(TypeError) as list_error:
            Rectangle.save_to_file((r1, r2))
        self.assertEqual('list_objs must be a list of instances',
                         str(list_error.exception))

    def test_save_to_file_correct(self):
        """ Tests correct input """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([r1, r2])
        desc = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' +
                ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        self.assertIsInstance(desc, str)

        with open('Rectangle.json', encoding='utf-8') as my_file:
            self.assertEqual(len(my_file.read()), len(desc))

    def test_from_json_string_none_one(self):
        """ Tests if json_string is None """
        json_object = Rectangle.from_json_string(None)
        self.assertEqual(json_object, '[]')

    def test_from_json_string_none_two(self):
        """ Tests if json_string is empty """
        json_object = Rectangle.from_json_string('')
        self.assertEqual(json_object, '[]')

    def test_from_json_string_correct(self):
        """ Test correct input """
        obj_string = '[{"height": 4, "width": 10}, {"height": 7, "width": 1}]'
        json_object = Rectangle.from_json_string(obj_string)

        self.assertIsInstance(obj_string, str)
        self.assertEqual(json_object, [{'height': 4, 'width': 10},
                                       {'height': 7, 'width': 1}])
        self.assertIsInstance(json_object, list)

    def test_create_rectangle(self):
        """ Correct input for rectangle cls """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()

        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r2, Rectangle)

    def test_create_square(self):
        """ Correct input for rectangle cls """
        r1 = Square(5)
        r1_dictionary = r1.to_dictionary()

        r2 = Square.create(**r1_dictionary)
        self.assertIsInstance(r2, Square)


if __name__ == '__main__':
    unittest.main()
