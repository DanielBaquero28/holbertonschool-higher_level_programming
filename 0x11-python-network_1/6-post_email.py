#!/usr/bin/python3
""" Importing necessay modules """
import requests
import sys


if __name__ == '__main__':
    req = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    content = req.text
    print(content)
