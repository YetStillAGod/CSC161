#Zian Kang, Homework 2: Numbers. Takes as input A and outputs estimated square root of A

def main():
	print("This program calculates the square root of a given number using the secant method.")
	num = float(input("What is the number for which you want to calculate the square root? "))
	time = int(input("How many iterations do you want to use? "))
	num0 = num / 5
	num1 = num / 10
	root = pow(num,0.5)
	for i in range(time): 
		approx = num0 - (num0**2 - num)/(num0 + num1)
		n = abs(approx - root)
		num1 = num0
		num0 = approx
		print(i+1 , approx , n)
	print("My guess for the square root of", num, "is", approx)
	print("The difference between my guess and the real result is" , n)

if __name__ == "__main__":
	main()