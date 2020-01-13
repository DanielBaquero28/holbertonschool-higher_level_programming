#!/usr/bin/python3
""" Importing necessary modules """
import requests
import sys


if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    e = req.status_code
    print("Error code: {}".format(e))
