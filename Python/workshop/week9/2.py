def is_leap_year(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

def main():
	year = int(input("input year for calculation: "))
	if is_leap_year(year) == True: 
		print("it is leap year")
	else: 
		print("it is not leap year")

if __name__ == '__main__':
	main()