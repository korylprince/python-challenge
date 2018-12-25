# http://www.pythonchallenge.com/pc/def/peak.html
import pickle
import sys

import util

soup = util.get_url_soup("http://www.pythonchallenge.com/pc/def/peak.html")
data_file = soup.find("peakhell").attrs["src"]
data = util.get_url("http://www.pythonchallenge.com/pc/def/" + data_file)
obj = pickle.loads(data.encode("utf8"))

for y in obj:
    for x in y:
        sys.stdout.write(x[0] * x[1])
    sys.stdout.write("\n")

util.print_url("channel")
