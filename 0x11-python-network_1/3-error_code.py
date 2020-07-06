#!/usr/bin/python3
"""Module that sends a request to url and display the body of response
"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    req = urllib.request.Request(URL)
    try:
        with urllib.request.urlopen(req) as response:
            res = response.read()
            print(res.decode('utf8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.getcode())
