def main():
	num_char = 0
	upp_char = 0
	low_char = 0
	spa_char = 0
	non_al_char = 0
	sentence = input("type a sentence: ")
	for i in range(len(sentence)):
		asc = ord(sentence[i])
		if asc == 32:
			spa_char += 1
		elif asc >= 33 and asc <= 47:
			non_al_char += 1
		elif asc >= 48 and asc <= 57:
			num_char += 1
		elif asc >= 58 and asc <= 64:
			non_al_char += 1
		elif asc >= 65 and asc <= 90:
			upp_char += 1
		elif asc >= 91 and asc <= 96:
			non_al_char += 1
		elif asc >= 97 and asc <= 122:
			low_char += 1
		elif asc >= 123 and asc <= 126:
			non_al_char += 1
	print("Number of number characters:", num_char, "\nNumber of uppercase characters:", upp_char, "\nNumber of lowercase characters:", low_char, "\nNumber of spacing characters:", spa_char, "\nNumber of non-alphanumeric characters:", non_al_char)

if __name__ == '__main__':
	main()