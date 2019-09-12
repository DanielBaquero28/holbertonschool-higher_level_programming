#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    for num_diff in argv[1:]:
        sum += int(num_diff)
    print(sum)
