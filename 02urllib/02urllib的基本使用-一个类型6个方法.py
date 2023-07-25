import urllib.request
# 使用urllib获取百度源码

# 1.定义url
url = "https://ww.baidu.com"

# 2.模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型
print(type(response))

# 六个方法
# 1.按照一个字节一个字节读
response.read()
# 2.
response.readline()
# 3.
response.readlines()
# 4.
response.getcode()
# 5.
response.geturl()
# 6.获取状态信息
response.getheaders()
