# http://www.pythonchallenge.com/pc/def/peak.html
import urllib2
import pickle
import sys

# get data and unpickle it
data = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
p = pickle.loads(data)

# do a little guessing
for x in p:
    for y in x:
        sys.stdout.write(y[0]*y[1])
    sys.stdout.write('\n')
