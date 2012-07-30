# http://www.pythonchallenge.com/pc/return/mozart.html, un=huge,pw=file
import urllib2,base64
import StringIO
import Image

request = urllib2.Request("http://www.pythonchallenge.com/pc/return/mozart.gif")
base64string = base64.encodestring('%s:%s' % ('huge', 'file')).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   

data = StringIO.StringIO(urllib2.urlopen(request).read())
pic = Image.open(data)
indices = []

# find where marker is
new = Image.new("RGB",(640,480))
for y in xrange(0,480):
    tempindices = []
    for x in xrange(0,640):
        if pic.getpixel((x,y)) == 195:
            tempindices.append(x)
    indices.append(tempindices[-1]-5)

#remap picture
for index in xrange(0,len(indices)): #index is y
    for x in xrange(0,640):
        try:
            new.putpixel((x,index),pic.getpixel((x+indices[index],index)))
        except IndexError:
            new.putpixel((x,index),pic.getpixel((x+indices[index]-640,index)))
new.show()
