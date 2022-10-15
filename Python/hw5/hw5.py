#Zian Kang, homework 5: functions

def to_numbers(num_list):
	for i in range(len(num_list)):
		num_list[i] = int(num_list[i].strip("\n"))
	return(num_list)

def sum_list(nums):
	Sum = sum(nums)
	return(Sum)

def square_each(nums):
	for i in range(len(nums)):
		nums[i] = (int(nums[i])) ** 2
	result = sum_list(nums)
	print("The sum of the squares of the numbers in the file is", result)

def main():
	name = str(input("Please enter the file name: "))
	file = open(name, "r")
	numbers = file.readlines()
	nums = to_numbers(numbers)
	square_each(nums)
	file.close()

if __name__ == '__main__':
	main()