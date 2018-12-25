# http://www.pythonchallenge.com/pc/def/equality.html
import re

import util

code = util.get_url_comments("http://www.pythonchallenge.com/pc/def/equality.html")[0]

solution = re.findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", code)
util.print_url("".join(solution))
