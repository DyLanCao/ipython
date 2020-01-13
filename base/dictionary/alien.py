
alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("change the value of dirctiony")
alien_0['color'] = 'blue'
print(alien_0)

print("delete one pair button")
del alien_0['color']
print(alien_0)

