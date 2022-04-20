import sys


strs = 'jkdfkgkjdfkjgdkjgdkjfkggdfgkjdfkgjhjdsjkgdjgffgkjjfgklgfhklhfgklgfklklhfgklgfklnxnxcmnxcsdjfsdfkjrtertetretterteterthjgjkliyirtirty'

dic = {}

for s in strs:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

for k, v in dic.items():
    print('字母 %s 出现的次数为：%s' % (k, v))
