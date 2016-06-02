import hashlib


o = open('C:/Users/jacob/Documents/GitHub/MadHasher/directory/lines.txt')
for lines in o:
    print(lines, end='')

h = hashlib.md5()
h.update(o)
print(h.hexdigest())###

