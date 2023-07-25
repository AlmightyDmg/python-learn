def f1():
    print("欢迎光临")


f1()

def mySum(a,b):
    print(a + b)
# 位置参数 按照位置对应传参
mySum(100,200)
# 关键字传参
mySum(b=200, a=100)


def myReturnSum(a, b):
    return a+b

print(myReturnSum(12,3))

