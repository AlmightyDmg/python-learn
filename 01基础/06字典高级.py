person = {"name": "张三", "age": 18}

print(person["name"])
print(person["age"])

# 不能使用 person.name 的方式
print(person.get("name"))

# 修改
person["name"] = "法外狂徒"

# 添加
person["sex"] = True

print(person["sex"])

# 删除
# del
#     删除某个元素
#     删除整个字典
del person["age"]
del person
# clear
#     清空字典 但是保留原对象
person.clear()

# 字典的遍历
# 1.遍历字典的key
for key in person.keys():
    print(key)
# 2.遍历字典的value
for value in person.values():
    print(value)
# 3.遍历字典key和value
for key, value in person.items():
    print(key + ":" + value)
# 4.遍历字典的项/元素
for item in person.items():
    print(item)

