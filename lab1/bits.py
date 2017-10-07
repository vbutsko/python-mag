def set_bit(num, k):
	return change_bit(num, k, '1')

def clear_bit(num, k):
	return change_bit(num, k, '0')

def test_bit(num, k, bit):
	return (num << k) % 2 == 1

def change_bit(num, k, bit):
	num_str = bin(num)[2:]
	array = []
	array.append(bin(num)[:2])
	if len(num_str) > k:
		array.append(num_str[ : len(num_str) - k - 1])
		array.append(bit)
		array.append(num_str[len(num_str) - k:])
	else:
		array.append(bit)
		for _ in range(k - 1 - len(num_str)): 
			array.append('0')
		array.append(num_str)
	return int(''.join(map(str, array)), 2)