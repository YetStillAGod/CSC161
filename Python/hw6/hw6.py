# Zian Kang, homework 6

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

def is_valid_date(date, month, year):
	if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
		if date <= 31 and date >= 1:
			return True
		else:
			return False
	elif month == 2:
		leap = is_leap_year(year)
		if leap == True:
			if date <= 29 and date >= 1:
				return True
			else:
				return False
		else:
			if date <= 28 and date >= 1:
				return True
			else:
				return False
	elif month == 4 or month == 6 or month == 9 or month == 11:
		if date <= 30 and date >= 1:
			return True
		else:
			return False
	else:
		return False

def main():
	date = input("Please enter a date (mm/dd/yyyy): ")
	mdy = date.split("/")
	m = int(mdy[0])
	d = int(mdy[1])
	y = int(mdy[2])
	valid = is_valid_date(d, m, y)
	if valid == True:
		print(date, "is valid")
	elif valid == False:
		print(date, "is not valid")

if __name__ == '__main__':
	main()
