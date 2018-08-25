#!/usr/bin/env python3

a = [23, 45, 1, -3434, 43624356, 234]
a.append(45)
print(a)

a.insert(0,1)
print(a)

a.insert(0,111)
print(a)


a.remove(234)
print(a)

a.reverse()
print(a)

print("count:%d"%(a.count(45)))
