# http://www.pythonchallenge.com/pc/def/map.html

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

from string import maketrans

int = "abcdefghijklmnopqrstuvwxyz"
outt = "cdefghijklmnopqrstuvwxyzab"
table = maketrans(int, outt)
print text.translate(table);
