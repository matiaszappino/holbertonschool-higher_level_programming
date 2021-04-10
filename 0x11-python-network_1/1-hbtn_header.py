#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL 
and displays the value of the X-Request-Id variable found in 
the header of the response """


import urllib.request
import sys

if __name__ == '__main__':
        with urllib.request.urlopen(sys.argv[1]) as response:
                html = response.read()
        headers_dict = dict(response.headers)
        print(headers_dict.get("X-Request-Id"))
