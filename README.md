# bigdict
When processing the data is greater than the physical memory, you can use the "bigdict", just as the use of Python built-in dictionary.

当处理的数据大于物理内存时，可以使用 “bigdict” ，就像使用python内置字典一样。 

适用python版本2.6以上3.0以下。


# First

git clone https://github.com/sdz7121211/bigdict

copy bigdict to your project path.

# demo

# BigDict 的初始化

tester = bigdict()

argv_dict = bigdict({"a": "b"})

# update 方法测试

tester.update(argv_dict)

# 赋值测试

tester["test"] = "testdddd"

tester["test"] = "test2222"

# setdefault 方法测试

print tester.setdefault("test", "aaaaa")

# keys、values、items 方法测试

print tester.keys()

print tester.values()

print tester.items()

# len属性测试

print len(tester)

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



