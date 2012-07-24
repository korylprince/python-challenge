# http://www.pythonchallenge.com/pc/return/5808.html, un=huge,pw=file 
import urllib2,base64
import StringIO
import Image

request = urllib2.Request("http://www.pythonchallenge.com/pc/return/cave.jpg")
base64string = base64.encodestring('%s:%s' % ('huge', 'file')).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   

data = StringIO.StringIO(urllib2.urlopen(request).read())
pic = Image.open(data)

odd = Image.new("RGB",(320,240))

for x in xrange(0,640,2):
    for y in xrange(0,480,2):
        odd.putpixel((x/2,y/2),pic.getpixel((x,y)))
odd.show()
