#!/usr/bin/python3
""" Importing necessary modules """
import sys
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print (html.get('X-Request-Id'))
