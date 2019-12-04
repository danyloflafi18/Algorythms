def convert_num(arr):
	converted_num = 0
	for i in range(len(arr)):
		converted_num += 2 ** (len(arr) - i - 1) * arr[i]
	return converted_num

def is_pow(convert_num, number_that_has_pow):
	if number_that_has_pow == 1:
		return convert_num == 1
	pow = 1
	while pow < convert_num:
		pow *= number_that_has_pow
	return pow == convert_num


def solve(arr, num):
	if is_pow(convert_num(arr), num):
		return 1
	buffer = []
	for i in range(len(arr)):
		amount = 0
		cond = arr[i]
		if cond:
			if is_pow(convert_num(arr[:i]), num):
				amount += solve(arr[i:], num) + 1
				buffer.append(amount)
	if buffer == []:
		return 9999999999
	else:
		return min(buffer)


if __name__ == '__main__':
	arr1 = [1, 1, 1, 1, 1, 0, 1]
	print("Expected 1 ->", solve(arr1, 5))

	arr2 = [1, 0, 1, 1, 0, 1, 1, 0, 1]
	assert 3 == solve(arr2, 5)

	arr3 = [1, 1, 0, 0, 1, 1, 0, 1, 1]
	assert 3 == solve(arr3, 5), "No combiinations"

	arr4 = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1,
			0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0,
			0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1,
			1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0,
			1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1,
			0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0,
			1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1,
			0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1]
	result = solve(arr4, 7)
	assert 6 == result, "Expected 6, got " + str(result)
