#!/usr/bin/python3
""" Module that takes URL and an email Sends Post req
    to URL with mail as param and display response body
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    Mail = sys.argv[2]
    value = {'email': Mail}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(URL, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('ascii'))
