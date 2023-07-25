import urllib.parse

data = {
    'name': '周杰伦',
    'sex': '男',
    'location': '中国台湾'
}

quoteData = urllib.parse.urlencode(data)
print(quoteData)