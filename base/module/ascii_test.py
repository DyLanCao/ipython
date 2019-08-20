# pythoon3

c = input("Please input a char: ")
a = int(input("Please input a ascii:"))
while True:
	if a < 0:
		print("ascii is wrong, Plese try again")
		a = int(input("Please input a ascii:"))
	elif a > 1000:
		print("ascii is wrong, Plese try again")
		a = int(input("Please input a ascii:"))
	else:
		break

print(" this is a ascii test")
print("assic is:",ord(c))
print(" char is:", chr(a))

