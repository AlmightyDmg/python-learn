import urllib.request

url = "https://www.baidu.com"


# 当访问 https 的时候 会遭遇到 反爬虫 因此返回的数据是不正确的，需要在请求的时候 request中加上 headers
# response = urllib.request.urlopen(url)
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)
