def recursive_sum(arr):
    if len(arr) == 0:
        return 0

    return arr.pop(0) + recursive_sum(arr)


def recursive_count(arr):
    if len(arr) == 0:
        return 0

    return 1 + recursive_count(arr[1:])


def recursive_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        sum_max = recursive_max(arr[1:])
        return arr[0] if arr[0] > sum_max else sum_max
