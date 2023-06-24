import meo

wds = []
for p in [
    './Blasting-dictionary/3389爆破字典.txt',
    './Blasting-dictionary/NT密码.txt',
    './Blasting-dictionary/自己收集的密码.txt',
    './Blasting-dictionary/突破密码.txt',
    './Blasting-dictionary/渗透字典.txt',
    './Blasting-dictionary/常用密码.txt',
    './Blasting-dictionary/top100password.txt',
]:
    _lines = meo.load_file(p)
    _lines = meo.auto_decode(_lines).split("\n")
    for line in _lines:
        line = line.strip()
        if line:
            wds.append(line)
lines = list(set(wds))
meo.to_file("./rootphantomer.txt", '\n'.join(lines))