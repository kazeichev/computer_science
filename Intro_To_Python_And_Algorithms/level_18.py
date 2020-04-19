def BiggerGreater(string):
    result = bubble_sort(list(string), list(), False, len(string))

    if not result.get('is_magic'):
        return ''

    combinations = result.get('combinations')
    combinations.sort()

    for i in combinations:
        if i > string:
            return i


def bubble_sort(chars, combinations, is_magic, n):
    for i in range(len(chars) - 2, -1, -1):
        if chars[i + 1] > chars[i]:
            chars[i + 1], chars[i] = chars[i], chars[i + 1]
            combinations.append(''.join(chars[:]))
            is_magic = True

    if n > 0:
        bubble_sort(chars, combinations, is_magic, n - 1)

    return dict({'combinations': combinations, 'is_magic': is_magic})
