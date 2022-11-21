import random

'''
def dice():
	n = random.random()
	if n > 0 and n < 1/6:
		p = 1
	elif n >= 1/6 and n < 1/3:
		p = 2
	elif n >= 1/3 and n < 5/13:
		p = 3
	elif n >= 5/13 and n < 2/3:
		p = 4
	elif n >= 2/3 and n < 5/6:
		p = 5
	elif n >= 5/6 and n < 1:
		p = 6
	return p

def game():
	n1 = dice()
	n2 = dice()
	if n1 + n2 == 7 or n1 + n2 == 11:
		return(1)
	elif n1 + n2 == 2 or n1 + n2 == 3 or n1 + n2 == 12:
		return(0)
	else:
		n = n1 + n2
		while True:
			n1 = dice()
			n2 = dice()
			if n1 + n2 == 7:
				return(0)
			elif n1 + n2 == n:
				return(1)
			else:
				continue


def main():
	m = int(input("number of rolls: "))
	n = 0
	for i in range(m):
		p = game()
		n += p
	print("Probability of winning is {:.2%}".format(n / m))

'''

def card():
	n = random.random()
	if n > 0 and n < 1/13:
		p = 1
	elif n >= 1/13 and n < 2/13:
		p = 2
	elif n >= 2/13 and n < 3/13:
		p = 3
	elif n >= 3/13 and n < 4/13:
		p = 4
	elif n >= 4/13 and n < 5/13:
		p = 5
	elif n >= 5/13 and n < 6/13:
		p = 6
	elif n >= 6/13 and n < 7/13:
		p = 7
	elif n >= 7/13 and n < 8/13:
		p = 8
	elif n >= 8/13 and n < 9/13:
		p = 9
	elif n >= 9/13 and n < 1:
		p = 10
	return p

def dealer():
	n = 0
	ace = False
	while True:
		p = card()
		n += p
		if p == 1:
			ace = True
		if ace == True and n + 10 >= 17 and n + 10 <= 21:
			return(0)
		elif n >= 17 and n <= 21:
			return(0)
		elif n > 21:
			return(1)

def main():
	m = int(input("number of games: "))
	n = 0
	for i in range(m):
		p = dealer()
		n += p
	print("Probability of bust is {:.2%}".format(n / m))

if __name__ == '__main__':
	main()
