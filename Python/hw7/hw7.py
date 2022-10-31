#Zian Kang, homework 7: Loops and Booleans

'''
def get_input():
	while True:
		number = input("Please enter a positive integer: ")
		num = list(number)
		for i in range(len(num)):
			if ord(num[i]) < 48 or ord(num[i]) > 57:
				is_int = False
				if num[0] == "-":
					if ord(num[i]) < 48 or ord(num[i]) > 57:
						is_int = False
						break
					else:
						is_int = True
						break
				i += 1
				if is_int == True:
					print("The integer must be positive.")
				else:
					print("Bad input!")
			else:
				n = int(number)
				return n
'''

def get_input():
	while True:
		b_in = False
		n_int = False
		p_int = False
		number = input("Please enter a positive integer: ")
		num = list(number)
		for i in range(len(num)):
			if num[0] == "-":
				for m in range(len(num) - 1):
					if (ord(num[m + 1]) < 48 or ord(num[m + 1]) > 57):
						b_in = True
						break
					else:
						n_int = True
						continue
			else:
				if ord(num[i]) >= 48 and ord(num[i]) <= 57:
					p_int = True
					continue
				else:
					b_in = True
					break
			if b_in == True:
				break
		if n_int == True:
			if b_in == True:
				print("Bad input!")
			else:
				print("The integer must be positive.")
		elif p_int == True:
			if b_in == True:
				print("Bad input!")
			else:
				break
		elif n_int == False and p_int == False and b_in == True:
			print("Bad input!")
	n = int(number)
	return n

def lagrange(n):
	m = int(pow(n, 0.5)) + 1
	for a in range(m):
		for b in range(m):
			for c in range(m):
				for d in range(m):
					if a ** 2 + b ** 2 + c ** 2 + d ** 2 == n:
						return [a, b, c, d]
					else:
						continue

def main():
	num = int(get_input())
	result = lagrange(num)
	print(result[0], result[1], result[2], result[3])

if __name__ == '__main__':
	main()

