#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]

    url = "https://api.github.com/user"

    auth = (username, access_token)

    r = requests.get(api_url, auth=auth)

    if r.status_code == 200:
        user_data = r.json()
        print(f"{user_data['id']}")
    else:
        print("None")
