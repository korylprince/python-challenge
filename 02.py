# http://www.pythonchallenge.com/pc/def/ocr.html
from collections import defaultdict

import util

code = util.get_url_comments("http://www.pythonchallenge.com/pc/def/ocr.html")[1]

charCount = defaultdict(int)
for c in code:
    charCount[c] += 1

string = ""
for c in code:
    if charCount[c] < 10:
        string += c

util.print_url(string)
