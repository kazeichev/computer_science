def Football(f, n):
    if sorted(f) == f:
        return False

    return iterate_sort(f, 0) or reverse_sort(f, 0)


def reverse_sort(array, n):
    reference = sorted(array)
    is_sorted_successfully = False

    if n > len(array):
        return is_sorted_successfully

    for i in range(0, len(array)):
        new_array = array[:]
        new_array[n:i + 1] = reversed(new_array[n:i + 1])

        if reference == new_array:
            is_sorted_successfully = True
            break

    if is_sorted_successfully is not True:
        return reverse_sort(array, n + 1)
    else:
        is_sorted_successfully = True
        return is_sorted_successfully


def iterate_sort(array, n):
    reference = sorted(array)
    is_sorted_successfully = False

    if n == len(array):
        return is_sorted_successfully

    for i in range(0, len(array)):
        new_array = array[:]
        new_array[n], new_array[i] = new_array[i], new_array[n]

        if reference == new_array:
            is_sorted_successfully = True
            break

    if is_sorted_successfully is not True:
        return iterate_sort(array, n + 1)
    else:
        is_sorted_successfully = True
        return is_sorted_successfully
