#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        print("Exception: Unknown format code 'd' for object of type 'str'")
        return (False)
    else:
        return (True)
