import numpy as np

left = []
right = []

data1 = [12,12,12,12,12,12,12]
data2 = [12,12,12,12,12,12,12]
data3 = []
for item in data1:
    left.append(item)

for item1 in data2:
    right.append(item1)

aleft = np.array(left)
bleft = np.array(right)

cleft = aleft - bleft
dleft = aleft + bleft
print("list a sub list b:")
print(cleft)
print("list a add list b:")
print(dleft)
print("list a append list b:")
cleft = data1 + data2
data1.append(data2)
print(cleft)
print(data1)
print("list a extend list b:")
data3.extend(data2)
print(data3)
