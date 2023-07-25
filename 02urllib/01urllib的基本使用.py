import urllib.request
# 使用urllib获取百度源码

# 1.定义url
url = "https://ww.baidu.com"

# 2.模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 3.获取相应中的页面的源码
# read 返回字节形式的二进制数据 要将二进制数据转换为字符串（解码）
content = response.read().decode('utf-8')

# 4.打印数据
print(content)