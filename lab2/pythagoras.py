def get_pythagoras_triples(n):
    return [(x, y, z) for z in xrange(1, n + 1) for x in xrange(1, z) for y in xrange(1, z) if (x ** 2 + y ** 2 == z ** 2)]