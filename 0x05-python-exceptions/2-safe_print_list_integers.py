#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            print("list index out of range")
            raise
        except ValueError:
            pass
        except TypeError:
            pass
        else:
            nb_print += i

    print()
    return (nb_print)
