import sys

arr = [1,2,3,4,5,6,7,8,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
tst1 = len(arr)
test2 = hex(tst1)

print(test2[2:])
test3 = int(test2,0)
print(test3)
print(str(test2))
