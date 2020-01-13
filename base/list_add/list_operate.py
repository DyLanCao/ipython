#python3 list operate example

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(bicycles)
print(bicycles[1])
print(bicycles[-1])

message = "I like bicycles color is " + bicycles[1] + "and enjory it"
print(message)

bicycles.append('green')
print(bicycles)

bicycles.insert(0,'white')
print(bicycles)

del bicycles[3]
print(bicycles)

people_poped = bicycles.pop()
print(people_poped)

first_poped = bicycles.pop(0)
print(first_poped)


