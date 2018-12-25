# http://www.pythonchallenge.com/pc/return/romance.html:huge:file
import bz2
import re
import sys
import urllib.parse
import xmlrpc.client

import requests

import util


def url_code(code):
    return "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + str(code)


code = "12345"
url = url_code(code)
cookietext = ""
while True:
    sys.stdout.write("Getting code: {0}    \r".format(code))
    r = requests.get(url)
    text = r.text
    cookietext += r.cookies["info"]
    if "Divide" in text:
        code //= 2
        url = url_code(code)
        continue
    try:
        code = int(re.search(r"next busynothing is (\d+)", text).group(1))
        url = url_code(code)
    except AttributeError:
        break

data = urllib.parse.unquote_to_bytes(cookietext.replace("+", " "))
text = bz2.decompress(data)
print(text)
proxy = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(proxy.phone("Leopold"))

util.print_url("violin", "return")
print("http://www.pythonchallenge.com/pc/stuff/violin.php")
cookies = requests.cookies.RequestsCookieJar()
cookies.set("info", urllib.parse.quote_plus("the flowers are on their way"))
r = requests.get("http://www.pythonchallenge.com/pc/stuff/violin.php", auth=("huge", "file"), cookies=cookies)
print(r.text)
util.print_url("balloons", "return")
