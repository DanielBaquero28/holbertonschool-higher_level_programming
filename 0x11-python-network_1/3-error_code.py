#!/usr/bin/python3
""" Importing necessary modules """
from urllib import request, error
import sys


if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as response:
            page = response.read()
            print(page.decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
