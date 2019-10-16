#!/usr/bin/python3
import sys
import json

save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'
args = sys.argv[1:]

try:
    json_object = load_json(filename)
except FileNotFoundError:
    save_json(args, filename)
else:
    json_object.extend(args)
    save_json(json_object, filename)
