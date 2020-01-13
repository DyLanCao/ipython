
def passwd_test():
	count=5
	while count:
		passwd = input("Please input passwd:")
		if 123456 == passwd:
			print("hello world")
		else:
			count -=1
			print('password is wrong, you have'.format(count))
			continue

passwd_test();
