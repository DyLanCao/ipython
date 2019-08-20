#python3

test1 = lambda :True
# 切记这个是个函数，要加括号
print(test1())

test2 = lambda x: x + 1
print(test2(2))

test3 = (lambda x, y: x + y)(3,4)
# 切记默认参数已经加了，这里不需要加括号
print(test3)
