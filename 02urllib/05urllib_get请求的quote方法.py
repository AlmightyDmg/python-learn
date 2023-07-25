import urllib.request
import urllib.parse



# 需求：获取 https://www.baidu.com/s?wd=周杰伦 的网页源码
# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

# 请求header定制是为了解决第一个反爬手段 UA
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
# 将周杰伦三个字变为 Unicode 格式
name = urllib.parse.quote("周杰伦")

url = "https://www.baidu.com/s?wd=" + name
print(url)
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)
