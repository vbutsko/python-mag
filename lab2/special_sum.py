def calculate_special_sum(n):
    return sum([(x - 1) * x for x in xrange(2, n + 1)])
