# Быстрая сортировка O(n * log n)
def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    del arr[pivot_index]

    less = [i for i in arr if i <= pivot]
    greater = [i for i in arr if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)
