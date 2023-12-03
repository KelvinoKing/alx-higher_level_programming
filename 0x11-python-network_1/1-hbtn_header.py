#!/usr/bin/python3
"""imports urllib to handle http requests
import sys to handle arguments passed in script
"""
import sys
from urllib import request


if __name__ == "__main__":

    url = sys.argv[1]

    with request.urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')

    print(request_id)
