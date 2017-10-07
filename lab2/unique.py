def compress(array):
    result = {}
    for x in array:
        if x in result:
            result[x] += 1;
        else:
            result[x] = 1
    return result.items()
