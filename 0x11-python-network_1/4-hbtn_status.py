#!/usr/bin/python3
""" Importing necessary modules """
import requests


if __name__ == '__main__':
    req = requests.get('https://intranet.hbtn.io/status')
    content = req.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
