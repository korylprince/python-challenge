# http://www.pythonchallenge.com/pc/def/ocr.html
import BeautifulSoup
import urllib2

# get data
html = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
soup = BeautifulSoup.BeautifulSoup(html)
data = soup.findAll(text=lambda text:isinstance(text, BeautifulSoup.Comment))[1]

# loop through data
letters = []
repeat = []
for x in data:
    if x in repeat:
        try:
            letters.remove(x)
        # we don't care if it's not in there
        except:
            pass
    elif x not in letters and x not in repeat:
        repeat.append(x)
        letters.append(x)
print ''.join(letters)
