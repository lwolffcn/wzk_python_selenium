from urllib.request import urlopen
import re
from ftplib import FTP


def main()
    try:
        f = FTP('ftp.mozilla.org')
    except:
        pass

    try:
        f.login()
    except:
        pass
    f.dir()

# webpage = urlopen('http://www.python.org')
# text = webpage.read()
# # print(text)
# m = re.search(b'<a href="([^"]+)" (.*)?>about</a>', text, re.IGNORECASE)
# print(m.group())
# print(m.group(1))
# print(m.group(2))
# a = r'<a href="/about/" >About</a>'
# mm = re.search('<a href="([^"]+)" >about</a>', a, re.IGNORECASE)
# print(mm.group(1))
# bt = 'bat|bet|bit'
# mmm = re.match(bt, 'bat')
# print(mmm.group())
#
# n = re.search('foo', 'foofooofoooofoofoofoo')
# if n is not None: # 如果匹配成功，就输出匹配内容
#     print(n.group())