#Zian Kang homework 8: simulation and design

import random

random.seed(0)

def random_walk_2d(n):
	pos = [0,0]
	for i in range(n):
		rad = random.random()
		if rad < 0.25:
			pos[1] += 1
		elif rad >= 0.25 and rad < 0.5:
			pos[0] += 1
		elif rad >= 0.5 and rad < 0.75:
			pos[1] -= 1
		elif rad >= 0.75 and rad < 1:
			pos[0] -= 1
	return(pos)

def main():
	m = int(input("How many walks should I do? "))
	n = int(input("How many steps should I take on each? "))
	s = 0
	for i in range(m):
		res = random_walk_2d(n)
		l = pow(res[0] ** 2 + res[1] ** 2, 0.5)
		s += l
	fin = s / m
	print("Average distance from start: %0.2f" %fin)

if __name__ == '__main__':
	main()