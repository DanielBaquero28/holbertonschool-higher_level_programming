#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        nb_print = 0
        for i in range(x):
                try:
                        print("{}".format(my_list[i]), end="")
                except:
                        break
                else:
                        nb_print += 1

        print()
        return (nb_print)
