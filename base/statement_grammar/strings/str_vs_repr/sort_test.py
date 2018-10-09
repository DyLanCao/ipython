fruit_list = [
    ('apple', 2),
    ('banana', 5),
    ('coconut', 1),
    ('durian', 3),
    ('elderberries', 4)
]

import operator
#from operator import itemgetter

sorted_fruit = sorted(fruit_list, key=operator.itemgetter(0))
print sorted_fruit
sorted_fruit = sorted(fruit_list, key=operator.itemgetter(1))
print sorted_fruit
