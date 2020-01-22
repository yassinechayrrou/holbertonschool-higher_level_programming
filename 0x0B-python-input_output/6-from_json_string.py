#!/usr/bin/python3
import json
"""returns an object represented by a json"""


def from_json_string(my_str):
        return json.loads(my_str)
