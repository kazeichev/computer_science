def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop(0) + recursive_sum(arr)
