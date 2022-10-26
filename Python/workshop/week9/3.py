def main():
	age = int(input("citizen's age: "))
	city = int(input("citizenship: "))
	if age >= 30 and city >= 9: 
		print("good for Senate")
	else:
		print("not for Senate")
	if age >= 25 and city >= 7: 
		print("good for House")
	else:
		print("not for House")

if __name__ == '__main__':
	main()