def isPrime(n):

	for num in range(2,n):
		if n % num == 0:
			return False
	return True

def get_valid_input():
	''' Get valid integer more than equal to 3'''
	while(True): 
		try:
			num = int(input('Enter a number: '))
		except:
			print("I dont undersand that")
			continue
		else:
			if num < 3:
				print("Number must be more than 2")
				continue
			else:
				break
	return num

print('This program generates all the less than a given number')

n = get_valid_input()
print('List of prime number less than', n, 'are:')
for num in range(2,n):
	if isPrime(num):
		print(num)
