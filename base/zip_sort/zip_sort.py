#python3
# -- coding: utf-8 --
a = [3,9,2,24,1,6]
b = ['a','b','c','d','e']

c = zip(a,b)

print(type(c))

print(sorted(zip(a,b)))
#print(c.sort())

print(sorted(c,key = lambda x:x[1]))
