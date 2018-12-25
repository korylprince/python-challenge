# http://www.pythonchallenge.com/pc/return/mozart.html:huge:file
from PIL import Image

import util

img = util.get_url_image("http://www.pythonchallenge.com/pc/return/mozart.gif", auth=("huge", "file")).convert("RGB")

newimg = Image.new(img.mode, (img.width, img.height))

for line in range(img.height):
    pixels = [img.getpixel((x, line)) for x in range(img.width)]
    idx = pixels.index((255, 0, 255)) - 1
    pixels = pixels[idx:] + pixels[:idx]
    for x in range(img.width):
        newimg.putpixel((x, line), pixels[x])

newimg.show()
util.print_url("romance", "return")
