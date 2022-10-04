#Zian Kang Homework 4: Sequences

def main():
	name = str(input("Please enter the filename of the financial data: "))
	file = open(name, "r")
	text = file.readlines()
	for line in text:
		if line == text[0]:
			print("\nThe initial principal is: ${:0.2f}".format(float(line[10: int(len(line) - 1)])))
			princ = float(line[10: int(len(line) - 1)])
		elif line == text[1]:
			print("Annual percentage rate is: {:.1%}".format(float(line[9: int(len(line) - 1)])))
		elif line == text[2]:
			print("Length of the term: {:0.0f}".format(int(line[6:len(line)-1])), "\n\nYear Value\n{:4.0f}".format(0), " ${:0.2f}".format(princ), sep = "")
		else:
			for i in range(len(text)):
				if line == text[i]:
					print("{:4.0f}".format(i - 2), "${:0.2f}".format(float(line)))
	file.close()

if __name__ == '__main__':
	main()
