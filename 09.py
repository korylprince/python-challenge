# http://www.pythonchallenge.com/pc/return/good.html:huge:file
import matplotlib.pyplot as plt

import util

comments = util.get_url_comments("http://www.pythonchallenge.com/pc/return/good.html", auth=("huge", "file"))[1].split("\n\n")

first = [-int(n) for n in ("".join(comments[1].splitlines()[1:])).split(",")]
second = [-int(n) for n in ("".join(comments[2].splitlines()[1:])).split(",")]

plt.scatter(first[0::2], first[1::2])
plt.plot(first[0::2], first[1::2])
plt.scatter(second[0::2], second[1::2])
plt.plot(second[0::2], second[1::2])
plt.show()

util.print_url("bull", "return")
