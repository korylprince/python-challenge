# # http://www.pythonchallenge.com/pc/return/evil.html, un=huge,pw=file 
import urllib2,base64
import Image
import StringIO

request = urllib2.Request("http://www.pythonchallenge.com/pc/return/evil2.gfx")
base64string = base64.encodestring('%s:%s' % ('huge', 'file')).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   

data = urllib2.urlopen(request).read() 

open('/tmp/pic1','w').write(data[0::5])
open('/tmp/pic2','w').write(data[1::5])
open('/tmp/pic3','w').write(data[2::5])
open('/tmp/pic4','w').write(data[3::5])
open('/tmp/pic5','w').write(data[4::5])
print "see /tmp/pic[1-5] for images"
