#!/usr/bin/python3
"""import requests and sys
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"

    data = {'q': letter}

    r = requests.post(url, data=data)

    try:
        json_data = r.json()

        if json_data:
            print(f"{[json_data['id']]} {json_data['name']}")
        else:
            print("Not result")

    except ValueError:
        print("Not a valid JSON")
