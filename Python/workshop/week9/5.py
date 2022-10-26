def sig_num(n):	
	global a
	if n == 1:
		a = "one "
	elif n == 2:
		a = "two "
	elif n == 3:
		a = "three "
	elif n == 4:
		a = "four "
	elif n == 5:
		a = "five "
	elif n == 6:
		a = "six "
	elif n == 7:
		a = "seven "
	elif n == 8:
		a = "eight "
	elif n == 9:
		a = "nine "
	elif n == 0:
		a = "zero "
	return a

def ty(n):
	global b
	if (n - n % 10) / 10 == 2:
		b = "twenty "
	elif (n - n % 10) / 10 == 3:
		b = "thirty "
	elif (n - n % 10) / 10 == 4:
		b = "forty "
	elif (n - n % 10) / 10 == 5:
		b = "fifty "
	elif (n - n % 10) / 10 == 6:
		b = "sixty "
	elif (n - n % 10) / 10 == 7:
		b = "seventy "
	elif (n - n % 10) / 10 == 8:
		b = "eighty "
	elif (n - n % 10) / 10 == 9:
		b = "ninety "
	return b


def dou_num(n):
	global c
	if n - n % 10 == 10:
		if n == 10:
			c = "ten "
		elif n == 11:
			c = "eleven "
		elif n == 12:
			c = "twelve "
		elif n == 13:
			c = "thirteen "
		elif n == 14:
			c = "fourteen "
		elif n == 15:
			c = "fifteen "
		elif n == 16:
			c = "sixteen "
		elif n == 17:
			c = "seventeen "
		elif n == 18:
			c = "eighteen "
		elif n == 19:
			c = "nineteen "
	else:
		if n % 10 == 0:
			c = ty(n)
		else:
			c = ty(n).rstrip() + "-" + sig_num(n % 10)
	return c

def tri_num(n):
	global d
	p = n // 100
	q = n % 100
	if q <= 9 and q >= 1:
		d = sig_num(p) + "hundred and " + sig_num(q)
	if q == 0:
		d = sig_num(p) + "hundred "
	else:
		d = sig_num(p) + "hundred and " + dou_num(q)
	return d

def hundred(n):
	global e
	if n <= 9:
		e = sig_num(n)
	elif n <= 99 and n >= 10:
		e = dou_num(n)
	elif n <= 999 and n >= 100:
		e = tri_num(n)
	return e

def main():
	num = input("enter a number (up to 999,999,999,999,999): ")
	number = int(num)
	num = list(reversed(list(str(number))))
	l = len(num)
	suffix = {0 : "", 1 : "thousand ", 2 : "million ", 3 : "billion ", 4 : "trillion "}
	if l <= 3:
			word = hundred(number)
	else:
		re_word_ls = []
		for i in range (0, l, 3):
			if l - i == 1:
				value = int(num[i])
			elif l - i == 2:
				value = int(num[i]) + int(num[	i + 1]) * 10
			else:
				value = int(num[i]) + int(num[i + 1]) * 10 + int(num[i + 2]) * 100
			if value == 0:
				continue
			re_word_ls.append(hundred(value) + suffix[i // 3])
		if num[2] == "0" and num[0] != "0":
			re_word_ls.insert(1, "and ")
		word_ls = list(reversed(re_word_ls))
		word = "".join(word_ls)
	print(word)

if __name__ == '__main__':
	main()