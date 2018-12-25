# http://www.pythonchallenge.com/pc/def/oxygen.html
import re

import util

img = util.get_url_image("http://www.pythonchallenge.com/pc/def/oxygen.png")

pixels = []

for x in range(0, img.width, 7):
    p = img.getpixel((x, img.height // 2))
    if p[0] == p[1] and p[1] == p[2]:
        pixels.append(p[0])

text = "".join([chr(p) for p in pixels])
ords = eval(re.search(r"\[(?:\d+(?:, )?)+\]", text).group(0))
code = "".join([chr(o) for o in ords])
util.print_url(code)
