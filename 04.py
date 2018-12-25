# http://www.pythonchallenge.com/pc/def/linkedlist.php
import re
import sys

import util


def url_code(code):
    return "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(code)


code = 12345
url = url_code(code)
solution = None
while True:
    sys.stdout.write("Getting code: {0}    \r".format(code))
    text = util.get_url(url)
    if "Divide" in text:
        code //= 2
        url = url_code(code)
        continue
    try:
        code = int(re.search(r"next nothing is (\d+)", text).group(1))
        url = url_code(code)
    except AttributeError:
        solution = text
        break

util.print_url(solution.split(".")[0])
