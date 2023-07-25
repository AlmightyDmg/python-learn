# 创建 test.txt 文件
# 模式 w可写 r 可读
# open("test.txt", "w")

# 打开文件 "a" 表示追加操作
fp = open("../test.txt", "r")
#fp.write("hello world\n" * 5)
print(fp.read())

# 文件夹是不可以创建的

# 关闭文件
fp.close()


# 序列化和反序列化
import json

file = open("name.txt","w")

name_list = ["张三", "李四"]

# 序列化
# dumps()
names = json.dumps(name_list)
file.write(names)
# dump()
json.dump(name_list, file)

# 反序列化 json.loads  json.load
file.close()
