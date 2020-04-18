chars_combinations = list()
is_magic = False


def BiggerGreater(string):
    global chars_combinations
    global is_magic

    bubble_sort(list(string))

    if not is_magic:
        return ''

    chars_combinations.sort()

    for i in chars_combinations:
        if i > string:
            return i


def bubble_sort(chars):
    global chars_combinations
    global is_magic

    for i in range(len(chars) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if chars[i] > chars[j]:
                chars[j], chars[j + 1] = chars[j + 1], chars[j]
                chars_combinations.append(''.join(chars[:]))
                is_magic = True
                bubble_sort(chars)

    return chars_combinations
