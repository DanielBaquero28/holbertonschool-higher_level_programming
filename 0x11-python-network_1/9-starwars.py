#!/usr/bin/python3
""" Importing necessary modules """
import requests
import sys

if __name__ == '__main__':
    try:
        req = requests.get(
            'https://swapi.co/api/people/?search=' + sys.argv[1])
        null = None
        content = req.text
        dict_1 = eval(content)

        if len(dict_1) > 0:
            print("Number of results: {}".format(dict_1['count']))
            for search in dict_1['results']:
                print(search['name'])
        else:
            print("No result")
    except:
        print("Not a valid JSON")
