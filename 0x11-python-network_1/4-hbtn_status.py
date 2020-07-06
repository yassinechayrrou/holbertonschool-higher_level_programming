#!/usr/bin/python3
"""Module that fetches URL
"""

import requests

if __name__ == "__main__":
    #url = "https://intranet.hbtn.io/status"
    url = "http://0.0.0.0:5050/status"
    req = requests.get(url)
    print("Body response:")
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))
