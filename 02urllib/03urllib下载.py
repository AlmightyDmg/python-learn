import urllib.request

'''
下载网页
下载图片
下载视频
'''
# url_page = "http://www.baidu.com"
# url 为地址 filename为下载后保存的文件名字
# urllib.request.urlretrieve(url_page, "baidu.html")

url_image = "https://img1.baidu.com/it/u=2990432137,4145919565&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=750"
urllib.request.urlretrieve(url_image, "a.jpg")