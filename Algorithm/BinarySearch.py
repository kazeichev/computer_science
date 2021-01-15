# Бинарный поиск - O(Log n)
def binary_search(items, value):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2

        if items[mid] == value:
            return mid

        if mid < value:
            low = mid + 1
        else:
            high = mid - 1

    return None
