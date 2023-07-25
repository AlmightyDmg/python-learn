import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    #'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    #'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    #'Connection': 'keep-alive',
    #'Content-Length': '153',
    #'Content-Type': ' pplication/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=FAB97ED43DFADAEAFBBA5719F1E7574F; PSTM=1665474959; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=AAEA0A0D5030B0C1B601A799B568B550:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-131%3A; BA_HECTOR=0l24818g2kah0g2004a18k2a1ibuucu1p; ZFY=JLF4uXTHk5OxJYffNi1:AE99mU:Bpuv:By2I:Ax4Q0LzlgQ:C; BAIDUID_BFESS=AAEA0A0D5030B0C1B601A799B568B550:SL=0:NR=10:FG=1; delPer=0; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1690270972; H_PS_PSSID=36547_38643_38831_38943_39114_39039_38919_39089_26350_39132_39051_39100_39044; BCLID=10994490507056240854; BCLID_BFESS=10994490507056240854; BDSFRCVID=85kOJexroG0ZmSbflk7wMBK9xFweG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKK0mOTHv-F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=85kOJexroG0ZmSbflk7wMBK9xFweG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKK0mOTHv-F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvDqTrP-trf5DCShUFshtciB2Q-XPoO3KJADfOPb4vOjULIL448hU5f5mkf3fbgy4op8P3y0bb2DUA1y4vp0toW3eTxoUJ2-KDVeh5Gqq-KXU4ebPRiJPr9QgbqslQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD89DjKKD6PVKgTa54cbb4o2WbCQfI5O8pcN2b5oQT8lhJbaKt7WJ5vu5qkXMpQbeq06-lOUWJDkXpJvQnJjt2JxaqRC3JjOsl5jDh3MKToDb-oteltHB2Oy0hvctn6cShnCqfjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQh-p52f6LjJnuO3j; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvDqTrP-trf5DCShUFshtciB2Q-XPoO3KJADfOPb4vOjULIL448hU5f5mkf3fbgy4op8P3y0bb2DUA1y4vp0toW3eTxoUJ2-KDVeh5Gqq-KXU4ebPRiJPr9QgbqslQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD89DjKKD6PVKgTa54cbb4o2WbCQfI5O8pcN2b5oQT8lhJbaKt7WJ5vu5qkXMpQbeq06-lOUWJDkXpJvQnJjt2JxaqRC3JjOsl5jDh3MKToDb-oteltHB2Oy0hvctn6cShnCqfjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQh-p52f6LjJnuO3j; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1690272108; ab_sr=1.0.1_ZWE1YTY5MWVmZDQ4MDhlZTZlNjgzMWU0NTA2ZjNkNjJmM2QxZmJhNmM4ZDZmMjQxMDA1MzJmMTRjMWY1YzI3Y2JjOGEyZjBlMmY2MGIyYTlmY2IwNWMxZmUwMTliNWYxZDBkZjQ1MzlkNTQzZjMyZmZlOTI2NDI2ZTI3NmMxMjNjZDUwMjRhNjU1NWMwZTEwMGEwNWQzYWE0Zjg0OWEzYg==',
    #'Host': 'fanyi.baidu.com',
    #'Origin': 'https://fanyi.baidu.com',
    #'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=spider&keyfrom=baidu&smartresult=dict&lang=auto2zh',
    #'Sec-Fetch-Dest': 'empty',
    #'Sec-Fetch-Mode': 'cors',
    #'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'china',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '596529.915712',
    'token': '0a64f392f52560e755887497bd39d46',
    'domain': 'common',
    'ts': '1690271923435'
}

data = urllib.parse.urlencode(data).encode('utf-8')

# post的请求参数必须要进行编码
request = urllib.request.Request(url=url,data=data,headers=headers)

response = urllib.request.urlopen(request)

obj = json.loads(response.read().decode('utf-8'))
print(obj)
