def sort(array):
    if len(array) == 1:
        return array
    else:
        array_left = list(sort(array[:len(array) // 2]))
        array_right = list(sort(array[len(array) // 2:]))
        result = []
        while array_left and array_right:
            if array_left[0] < array_right[0]:
                result.append(array_left.pop(0))
            else:
                result.append(array_right.pop(0))
        result.extend(array_left) if array_left else result.extend(array_right)
        if isinstance(array, list):
            return result
        else:
            return tuple(result)
