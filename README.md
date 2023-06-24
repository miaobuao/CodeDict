# Code Dict

简化遍历密码字典的操作, 现已预置如下字典:
+ [Top1000](https://github.com/k8gege/PasswordDic.git)
+ [500万密码](https://github.com/r35tart/RW_Password.git)
+ [WPA密码](https://github.com/conwnet/wpa-dictionary.git)
+ [rootphantomer密码本](https://github.com/rootphantomer/Blasting_dictionary.git)

## 安装 - Install

```bash
pip install codedict
```

## 使用 - Usage

```python
from codedict import Codes

for code in Codes.top1000():
    print(code)
```