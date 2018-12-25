# http://www.pythonchallenge.com/pc/def/map.html
import string

import util

soup = util.get_url_soup("http://www.pythonchallenge.com/pc/def/map.html")
code = soup.findAll("font")[1].text.strip()

in_letters = string.ascii_lowercase
out_letters = in_letters[2:] + in_letters[:2]
table = str.maketrans(in_letters, out_letters)
print(code.translate(table))
util.print_url("map".translate(table))
