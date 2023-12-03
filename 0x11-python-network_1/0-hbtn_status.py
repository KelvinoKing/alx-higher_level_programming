#!/usr/bin/python3
"""imports urllib module for http connections
"""
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    html = response.read()

print("Body response:")
print("    - type: ", type(html))
print("    - content: ", html)
print("    - utf8 content: ", html.decode("utf-8"))
