# http://www.pythonchallenge.com/pc/return/evil.html:huge:file
import io

from PIL import Image, ImageFile

import util

# allow viewing truncated image
ImageFile.LOAD_TRUNCATED_IMAGES = True

data = util.get_url_file("http://www.pythonchallenge.com/pc/return/evil2.gfx", auth=("huge", "file")).read()
for i in range(5):
    with open("/tmp/{0}.jpg".format(i), "wb") as f:
        f.write(data[i::5])
    img = Image.open(io.BytesIO(data[i::5]))
    img.show()

util.print_url("disproportional", "return")
