def fizzbuzz(range_size):
	result_range =[];
	for x in range(range_size):
		result = "";
		if not x % 3:
			result += "Fizz";
		if not x % 5:
			result += "Buzz";
		if len(result) is 0:
			result = 2 * x;
		result_range.append(result);
	return result_range;

answers_range = fizzbuzz(25);
print (" ".join(map(str, answers_range)));