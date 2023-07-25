import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

data = {
    'kw':'spider'
}

data = urllib.parse.urlencode(data).encode('utf-8')

# post的请求参数必须要进行编码
request = urllib.request.Request(url=url,data=data,headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))
