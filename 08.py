# http://www.pythonchallenge.com/pc/def/integrity.html
import bz2

import util

comment = util.get_url_comments("http://www.pythonchallenge.com/pc/def/integrity.html")[0].strip()
username = (bz2.decompress(eval("b" + comment.splitlines()[0].strip()[4:]))).decode("utf8")
password = (bz2.decompress(eval("b" + comment.splitlines()[1].strip()[4:]))).decode("utf8")

print("http://www.pythonchallenge.com/pc/return/good.html:{0}:{1}".format(username, password))
