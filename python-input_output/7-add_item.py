#!/usr/bin/python3
"""Adds arguments in a Python list then saves it in a json representation"""
import json
import sys
save_item = __import__('5-save_to_json_file').save_to_json_file
load_item = __import__('6-load_from_json_file').load_from_json_file

try:
    items_list = load_item('add_item.json')
except Exception:
    items_list = []

item = sys.argv[1:]

with open('add_item.json', 'r+', encoding="utf-8") as f:
    save_item(item, 'add_item.json')
