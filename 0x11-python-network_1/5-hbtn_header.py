#!/usr/bin/python3
"""Module that take URL and sends a request to display X-Request-Id
"""

import requests
import sys
import pprint


if __name__ == "__main__":
    URL = sys.argv[1]
    r = requests.get(URL)
    print(r.headers['X-Request-Id'])
