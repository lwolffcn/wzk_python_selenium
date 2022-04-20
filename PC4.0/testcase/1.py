import urllib.request




# User-Agent是爬虫与反爬虫的第一步
# ua_headers = {'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'}
# 通过urllib2.Request()方法构造一个请求对象
# request = urllib.request.Request('http://wzk.36ve.com', headers=ua_headers)
request = urllib.request.Request('http://wzk.36ve.com')
response = urllib.request.urlopen(request)
html = response.read()
print(html)


# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0