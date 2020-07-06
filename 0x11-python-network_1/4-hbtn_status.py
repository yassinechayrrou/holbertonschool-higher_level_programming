#!/usr/bin/python3
"""Module that fetches URL"""

import requests


if __name__ == "__main__":
    URL = "https://intranet.hbtn.io/status"
    req = requests.get(URL)
    print("Body response:")
    print('\t-type: {}'.format(type(req.text)))
    print('\t-content: {}'.format(req.text))
