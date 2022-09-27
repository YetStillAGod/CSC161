#This function is for basic calculation.

def main():
	print("The codes are for basic calculation")
	for i in range(100):
		m = str(input("Please enter an arithmetic expression: "))
		n = eval(m)
		print(n)

if __name__ == "__main__":
	main()
