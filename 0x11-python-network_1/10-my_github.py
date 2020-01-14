#!/usr/bin/python3
""" Importing the necessary modules """
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    try:
        req = requests.get('https://api.github.com/user',
                           auth=HTTPBasicAuth(username, password))
        null = None
        false = False
        content = req.text
        dict_1 = eval(content)

        print("{}".format(dict_1['id']))
    except:
        print("None")
