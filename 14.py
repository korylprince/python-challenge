# http://www.pythonchallenge.com/pc/return/italy.html, un=huge,pw=file 
import urllib2,base64
import StringIO
import Image
import itertools

request = urllib2.Request("http://www.pythonchallenge.com/pc/return/wire.png")
base64string = base64.encodestring('%s:%s' % ('huge', 'file')).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   

data = StringIO.StringIO(urllib2.urlopen(request).read())
pic = Image.open(data)
#we map the pixels onto a spiral - down and dirty
new = Image.new("RGB",(100,100))


doubled_steps=200
directions=[(1,0), (0,1), (-1,0), (0,-1)] #right, down, left, up 
coor = (-1,0)
index = 0
while doubled_steps // 2 > 0:
    for direction in directions:
        count = doubled_steps // 2
        for step in range(count):
            coor = (coor[0] + direction[0], coor[1] + direction[1])
            new.putpixel(coor, pic.getpixel((index,0)))
            index += 1
        doubled_steps -= 1
new.show()
