# http://www.pythonchallenge.com/pc/def/channel.html
import re
import sys
import zipfile

import util

zip = zipfile.ZipFile(util.get_url_file("http://www.pythonchallenge.com/pc/def/channel.zip"))
code = "90052"
while True:
    comment = zip.getinfo(code + ".txt").comment
    sys.stdout.write(comment.decode("utf8"))
    with zip.open(code + ".txt") as f:
        try:
            text = f.read().decode("utf8")
            code = re.search(r"nothing is (\d+)", text).group(1)
        except AttributeError:
            break

util.print_url("hockey")
util.print_url("oxygen")
