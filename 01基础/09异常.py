try:
    open("aaa.txt")
except FileNotFoundError:
    print('系统正在升级')