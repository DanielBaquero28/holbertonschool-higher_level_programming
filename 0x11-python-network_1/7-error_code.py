#!/usr/bin/python3
""" Importing necessary modules """
import requests
import sys


if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    e = req.status_code
    content = req.text
    if e >= 400:
        print("Error code: {}".format(e))
    else:
        print(content)
