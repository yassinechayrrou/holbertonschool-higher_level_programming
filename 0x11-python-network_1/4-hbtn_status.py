#!/usr/bin/python3
"""Module that fetches URL
"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = requests.get(url)
    print("Body response:", end="")
    print('\n\t-type: {}'.format(type(req.text)))
    print('\t-content: {}\n'.format(req.text), end="")
