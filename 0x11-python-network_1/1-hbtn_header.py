#!/usr/bin/python3
"""python script that sends request to URL and displays
   X-Request-Id value in the header of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen("{}".format(sys.argv[1])) as response:
        print("{}".format(response.info()["X-Request-Id"]))
