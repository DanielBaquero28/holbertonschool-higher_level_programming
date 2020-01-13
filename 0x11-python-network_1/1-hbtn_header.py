#!/usr/bin/python3
""" Importing necessary modules """
import sys
import urllib.request


if __name__ == '__main__':
    """ Takes an URL, sends a request and displays value of X-Request-Id """
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print (html.get("X-Request-Id"))
