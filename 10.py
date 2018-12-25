# http://www.pythonchallenge.com/pc/return/bull.html:huge:file
import util


def spell_it_out(input):
    output = ""
    letter = None
    count = 0
    for lt in input:
        if count == 0:
            letter = lt
            count = 1
        elif lt == letter:
            count += 1
        else:
            output += "{0}{1}".format(count, letter)
            letter = lt
            count = 1
    output += "{0}{1}".format(count, letter)
    return output


code = "1"
for i in range(30):
    code = spell_it_out(code)

util.print_url(len(code), "return")
