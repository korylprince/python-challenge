# http://www.pythonchallenge.com/pc/return/bull.html, un=huge,pw=file

#This counts out the previous number 1, 11 (one 1), 21 (two 1s), etc


number = '1'
numbers = ['1']
while len(numbers)<31:
    strnum = ''
    index = 0
    count = 0
    prev = '0'
    while index <= len(number):
        if index == len(number):
            strnum += str(count)+prev
            break
        if prev == '0':
            prev = number[index]
            count = 1
            index += 1
        else:
            if prev == number[index]:
                count += 1
                index += 1
            else:
                strnum += str(count)+prev
                prev = number[index]
                count = 1
                index += 1
    numbers.append(strnum)
    number = strnum
print len(numbers[30])
