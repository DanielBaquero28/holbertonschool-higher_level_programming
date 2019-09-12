#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    sum = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, sum))
    sub1 = sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, sub1))
    mul1 = mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, mul1))
    div1 = div(a, b)
    print("{:d} / {:d} = {:d}".format(a, b, div1))
