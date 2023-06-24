from fileblock import Block

root = Block("./PasswordDic")

def get_words(root):
    root = Block(root)
    col = []
    for file in root.leaves:
        if file.extension == '.txt':
            col += file.get_file_contents('r', 'utf8').split('\n')
    col = list(set([cell.strip() for cell in col if cell.strip()]))
    return col

import meo
for root, output in [
    ("./PasswordDic", "./top1000.txt"),
    ("./wpa-dictionary", "./wpa.txt")
]:
    meo.to_file(output, "\n".join(get_words(root)))
