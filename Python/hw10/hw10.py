'''Zian Kang, Homework 10: Data Collections.'''

class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def get_rank(self):
		return self.rank

	def get_suit(self):
		return self.suit

	def bj_value(self):
		if self.rank > 10:
			return 10
		else:
			return self.rank

	def __repr__(self):
		num = ['Zero','Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
		if self.suit == 'd':
			return f'{num[self.rank]} of Diamonds'
		if self.suit == 'c':
			return f'{num[self.rank]} of Clubs'
		if self.suit == 'h':
			return f'{num[self.rank]} of Hearts'
		if self.suit == 's':
			return f'{num[self.rank]} of Spades'
def main():
	Card_t= {'c': [0,0,0,0,0,0,0,0,0,0,0,0,0,0], 'd':[0,0,0,0,0,0,0,0,0,0,0,0,0,0], 'h':[0,0,0,0,0,0,0,0,0,0,0,0,0,0], 's':[0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
	Card_n = {'c': [], 'd': [], 'h':[], 's':[]}
	while True:
		r = int(input('Enter rank, or 0 to stop: '))
		if r == 0:
			break
		else:
			suit = input('Enter suit: ')
			Card_n[suit].append(r)
			Card_t[suit][r] += 1


	print('\nYour sorted cards are')
	Card_n['c'].sort()
	Card_n['d'].sort()
	Card_n['h'].sort()
	Card_n['s'].sort()
	for key in Card_n:
		for i in range(len(Card_n[key])):
			print(Card(Card_n[key][i],key))

	print('\nThe total number of cards of each rank are')
	print('Clubs:',Card_t['c'])
	print('Diamonds:', Card_t['d'])
	print('Hearts:',Card_t['h'])
	print('Spades:',Card_t['s'])

if __name__ == "__main__":
    main()









