import re

f1 = open("asp.txt", 'w')
f2 = open("aspx.txt", 'w')
f3 = open("php.txt", 'w')
f4 = open("html.txt", 'w')
f5 = open("jsp.txt", 'w')
f6 = open("mdb.txt", 'w')
f7 = open("htm.txt", 'w')
f8 = open("txt.txt", 'w')
f9 = open("else.txt", 'w')
ff = open("all.txt",'r')

while 1:
    str = ff.readline()
    if len(str)<1:
        break
    if re.search(r'(.*)asp\n', str):
        f1.write(str)
    elif re.search(r'(.*)aspx\n', str):
        f2.write(str)
    elif re.search(r'(.*)php\n', str):
        f3.write(str)
    elif re.search(r'(.*)html\n', str):
        f4.write(str)
    elif re.search(r'(.*)jsp\n', str):
        f5.write(str)
    elif re.search(r'(.*)mdb\n', str):
        f6.write(str)
    elif re.search(r'(.*)htm\n', str):
        f7.write(str)
    elif re.search(r'(.*)txt\n', str):
        f8.write(str)
    else:
        f9.write(str)

ff.close()
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()