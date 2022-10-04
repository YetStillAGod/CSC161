
def main():# main is the identifier
	print("This program illustrates a chaotic function")
	x = float(input("Enter a number between 0 and 1: ")) # x is the identifier
	for i in range(10): #i is the identifier
		x = 3.9 * x * (1 - x) #expression
		print(x)


'''
Problem 3
def main():
	name = str(input("What is your name, please? "))
	print("Hello" , name, ", how are you today?")

if __name__ == "__main__":
	main()
'''

'''
Problem 4
def main():
	t = float(input("the temperature in Fahrenheit: "))
	v = float(input("the wind speed: "))
	W = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16
	print("the wind chill is:", W)

if __name__ == "__main__":
	main()
'''