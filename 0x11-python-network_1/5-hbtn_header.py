#!/usr/bin/python3
"""
A script that:
- takes in a URL,
- sends a request to the URL, and
Displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
