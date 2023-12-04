#!/usr/bin/python3
"""imports request and sys
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)

    if (r.status_code >= 400):
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
