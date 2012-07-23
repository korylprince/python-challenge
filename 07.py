# http://www.pythonchallenge.com/pc/def/oxygen.html
import urllib2
import StringIO
import Image

data = StringIO.StringIO(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read())
pic = Image.open(data)
codes = []
# loop through pixels about halfway down
for x in xrange(0,pic.size[0],7):
    pixel = pic.getpixel((x,45))
    # make sure it's greyscale
    if pixel[0] == pixel[1] == pixel[2]:
        codes.append(pixel[0])
print ''.join([chr(x) for x in codes])

# add in array from pic:
newcodes = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join([chr(x) for x in newcodes])
