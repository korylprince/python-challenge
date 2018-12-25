# http://www.pythonchallenge.com/pc/return/5808.html:huge:file
from PIL import Image

import util

img = util.get_url_image("http://www.pythonchallenge.com/pc/return/cave.jpg", auth=("huge", "file"))

even = Image.new(img.mode, (img.width // 2, img.height // 2))

for x in range(0, img.width // 2):
    for y in range(0, img.height // 2):
        even.putpixel((x, y), img.getpixel((x * 2, y * 2)))

even.show()

util.print_url("evil", "return")
