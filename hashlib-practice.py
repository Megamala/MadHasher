import hashlib


m = hashlib.md5()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
print(m.digest())
print(m.hexdigest())

o = 50
while o >= 12:
    o -= 1
    f = hashlib.sha256()
    f.update(b"Hello world")
    print(f.hexdigest())
