def calculate_gcd(a, b):
	return a if b is 0 else calculate_gcd(b, a % b)