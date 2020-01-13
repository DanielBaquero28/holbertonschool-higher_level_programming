#!/usr/bin/python3
""" Importing the necessary modules """
import sys
import requests


if __name__ == '__main__':
    try:
        req = requests.get(sys.argv[1])
        print(req.headers['X-Request-Id'])
    except:
        pass
