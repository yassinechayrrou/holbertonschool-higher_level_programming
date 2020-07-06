#!/usr/bin/python3
"""Module that fetches URL"""

import requests


if __name__ == "__main__":
    URL = "https://intranet.hbtn.io/status"
    req = requests.get(URL)
    print("Body response:")
    print("\t-type: {}\n\t-content: {}".format(type(req.text), req.text))
