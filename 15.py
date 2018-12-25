# http://www.pythonchallenge.com/pc/return/uzi.html:huge:file
import calendar
import datetime

import util

dates = []

for year in range(1006, 1996, 10):
    d = datetime.date(year, 1, 26)
    if d.isoweekday() == 1 & calendar.isleap(year):
        dates.append(d)

print("Who was born on {0}?".format(dates[-2]))
util.print_url("mozart", "return")
