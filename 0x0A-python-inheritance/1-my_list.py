#!/usr/bin/python3
class MyList(list):
    """ Inherits from list. """
    def print_sorted(self):
        """ Prints a list in ascendent order. """
        new_list = self.copy()
        new_list.sort()

        print(new_list)
