#!/usr/bin/python3
"""Python script that takes 2 arguments in order
to solve this challenge.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
