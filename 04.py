# http://www.pythonchallenge.com/pc/def/linkedlist.php
import urllib2
import re

nothing = '12345'

try:
    while True:
        data = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'.format(nothing)).read()
        print data
        # search for string, but capture number only
        search = re.search(r'next nothing is ([0-9]*)',data)
        nothing = search.group(1)
        print 'found: ', nothing
        # catch random entry
        if nothing == '16044':
            nothing = '8022'
            print 'nothing is now 8022'
except AttributeError:
    print 'No numbers found, last text was: ',data
