# http://www.pythonchallenge.com/pc/return/disproportional.html:huge:file
import xmlrpc.client

import util

proxy = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(proxy.phone("Bert"))
util.print_url("italy", "return")
