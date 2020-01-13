#!/usr/bin/python3
""" Importing necessary modules """
import requests
import sys


if __name__ == '__main__':
    data = {}
    data['q'] = ""
    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
    try:
        req = requests.post('http://0.0.0.0:5000/search_user', data=data)
        content = req.text
        dict_1 = eval(content)
        if len(dict_1) > 0:
            print("[{}] {}".format(dict_1['id'], dict_1['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
