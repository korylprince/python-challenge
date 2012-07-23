# http://www.pythonchallenge.com/pc/def/channel.html
import urllib2
import zipfile
import StringIO
import re

data = StringIO.StringIO(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip').read())
zip = zipfile.ZipFile(data)
nothing = '90052'
comments = []

try:
    while True:
        # get comment from file
        comments.append(zip.getinfo(nothing+'.txt').comment)
        str = zip.open(nothing + '.txt').read()
        print str

        # search for string, but capture number only
        search = re.search(r'[Nn]ext nothing is ([0-9]*)',str)
        nothing = search.group(1)
        print 'found: ', nothing
# stop when no more numbers are found
except AttributeError:
    pass
print ''.join(comments)
