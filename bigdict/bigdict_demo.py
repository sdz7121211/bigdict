# coding: utf-8
from bigdict import bigdict

# 唯一需要注意的是：改变从bigdict取出的“对象”，需要使用update方式显示的更新到磁盘上
# 唯一需要注意的是：改变从bigdict取出的“对象”，需要使用update方式显示的更新到磁盘上
# 唯一需要注意的是：改变从bigdict取出的“对象”，需要使用update方式显示的更新到磁盘上
# 三遍，三遍，三遍

# 测试自定义对象的保存
class testclass(object):

    def __init__(self, value):
        self.value = value

    def setValue(self, value):
        self.value = value

######### TEST #########

# BigDict 的初始化
null_dict = bigdict()
tester = bigdict({"a": "b"})
tester_1 = bigdict({"a": "d", "b": "f"})

# update 方法测试
tester.update(tester_1)
print tester.items()
tester.update({"a": "c"})
# 赋值测试
tester["test"] = "testdddd"
tester["test"] = "test2222"
# setdefault 方法测试
print tester.setdefault("test", "aaaaa")
print tester["test"]
print tester.setdefault("test", set([1, 3, 4]))
print tester.setdefault("test1", "aaaaa")
print tester.get("test", "sadfasfsadf")
print "test" in tester
print "testssss" in tester

# keys、values、items 方法测试
print tester.keys()
print tester.values()
print tester.items()

# pop方法测试
tester[1] = 2
print tester.popitem()
tester["pop"] = "opopopo"
print tester.pop("pop")
print tester.get("pop", "nopop")

# len属性测试
print len(tester)

print "ssssssss", tester.keys()
print "dddddddd", tester.values()

# in 操作测试
print "a" in tester
print "b" in tester
print [key for key in tester]
for key in tester:
    print "key", key

# clear 方法测试
tester.clear()
print len(tester)

# 迭代器测试
print list(tester.iterkeys())
print list(tester.itervalues())

# test cmp
test_1 = bigdict()
test_1[1] = 2
test_2 = bigdict()
test_2[1] = 2
print test_1 == test_2

i = testclass("sdfasfsa")

# tester是一个bigdict实例
tester["1"] = i
print tester["1"].value
print id(i)
print id(tester["1"])
print tester["1"].value
tester["1"].setValue("11111")
print tester["1"].value

