# http://www.pythonchallenge.com/pc/return/disproportional.html, un=huge,pw=file
import xmlrpclib

server_url = 'http://www.pythonchallenge.com/pc/phonebook.php'
server = xmlrpclib.Server(server_url)
# We phone bert because http://www.pythonchallenge.com/pc/return/evil4.jpg
print server.phone('Bert')
print '(or just italy)'
