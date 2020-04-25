def SherlockValidString(string):
    is_valid = False
    letters_count = get_letters_count(list(string))

    if check_validity(letters_count):
        is_valid = True
    else:
        for i in range(0, len(letters_count)):
            items = configure_items(letters_count, i)

            if check_validity(items):
                is_valid = True

    return is_valid


def configure_items(counts, n):
    counts = counts[:]
    counts[n] -= 1

    if counts[n] == 0:
        del counts[n]

    return counts


def check_validity(letters_count):
    is_valid = True

    for i in range(len(letters_count)):
        if i == len(letters_count) - 1:
            break

        if letters_count[i] != letters_count[i + 1]:
            is_valid = False
            break

    return is_valid


def get_letters_count(letters):
    counts = dict()

    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    return list({k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}.values())
