# http://www.pythonchallenge.com/pc/return/italy.html:huge:file
from PIL import Image

import util

img = util.get_url_image("http://www.pythonchallenge.com/pc/return/wire.png", auth=("huge", "file"))

newimg = Image.new(img.mode, (100, 100))

steps = 200
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
coords = (-1, 0)
i = 0
while steps // 2 > 0:
    for direction in directions:
        for step in range(steps // 2):
            coords = (coords[0] + direction[0], coords[1] + direction[1])
            newimg.putpixel(coords, img.getpixel((i, 0)))
            i += 1
        steps -= 1
newimg.show()

util.print_url("cat", "return")
util.print_url("uzi", "return")
