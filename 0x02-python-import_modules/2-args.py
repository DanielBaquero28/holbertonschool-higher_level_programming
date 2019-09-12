#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    print("{} argument{}".format(args, "s:" if args > 1 else "s." if args == 0
                                 else ":" if args == 1 else "."))
    for enum, arg in enumerate(argv[1:]):
        print("{:d}: {:s}".format(enum + 1, arg))
