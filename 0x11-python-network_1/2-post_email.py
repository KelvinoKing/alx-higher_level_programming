#!/usr/bin/python3
"""uses urllib and sys
"""
import sys
from urllib import request, parse


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode('utf-8')

    with request.urlopen(url, data=data) as response:
        content = response.read().decode('utf-8')
        print(content)
