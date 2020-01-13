#!/usr/bin/python3
""" Importing necessary modules """
from urllib import request, parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        page = response.read()
