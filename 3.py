# http://www.pythonchallenge.com/pc/def/equality.html
import BeautifulSoup
import urllib2
import re

# get data
html = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
soup = BeautifulSoup.BeautifulSoup(html)
data = soup.findAll(text=lambda text:isinstance(text, BeautifulSoup.Comment))[0]

# get patterns of aAAAbAAAa and string of b's
search = re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', data)
print ''.join([x[4] for x in search])
