from codedict import CodeLoader
from meo.utils import ScriptPath

path = ScriptPath(__file__).join("./test.txt").path
print("read: " + path)

loader = CodeLoader(path)

# return str
for i in loader:
    print(i)


# return bytes
for i in loader.bytes():
    print(i)
