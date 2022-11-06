#Zian Kang, homework 7: Loops and Booleans

def get_input():
	while True:
		try:
			n = int(input("Please enter a positive integer: "))
			if n > 0:
				return n
			else:
				print("The integer must be positive.")
		except:
			print("Bad input!")

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

