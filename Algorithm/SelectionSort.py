def find(arr, sort):
    element = arr[0]
    element_index = 0

    for i in range(1, len(arr)):
        if sort == 'asc' and arr[i] < element:
            element = arr[i]
            element_index = i
        elif sort == 'desc' and arr[i] > element:
            element = arr[i]
            element_index = i

    return element_index


def selection_sort(arr, sort='asc'):
    newArr = []

    for i in range(len(arr)):
        smallest_index = find(arr, sort)
        newArr.append(arr.pop(smallest_index))

    return newArr

