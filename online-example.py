import hashlib


def md5sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        while True:
            buf = f.read(1024)  # 128 is smaller than the typical filesystem block
            if not buf:
                break
        d.update(buf)
    return d.hexdigest()


print(md5sum('file-practice.py'))
