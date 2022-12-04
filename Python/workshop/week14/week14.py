import random

def shuffle(a):
	b = random.sample(a, len(a))
	return(b)

def main():
	ini_str = input("enter a list, separate by space: ")
	ini_list = ini_str.split()
	fin_list = shuffle(ini_list)
	print(fin_list)

if __name__ == '__main__':
	main()