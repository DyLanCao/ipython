import os

filenames = os.listdir('.')
print(filenames)

state = any(name.endswith('.py') for name in filenames)
print(state)

