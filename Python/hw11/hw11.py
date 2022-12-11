# Zian Kang, Homework 11: Algorithms

def reverse(s):
	if s == "":
		return s
	else:
		return reverse(s[1:]) + s[0]

def main():
	ini = input("Enter the string to reverse: ")
	fin = reverse(ini)
	print(ini, "reversed is", fin, sep = " ")

if __name__ == '__main__':
	main()