def BiggerGreater(string):
    sequence = list(string)
    permutations = list()
    permutation_found = True

    while permutation_found:
        permutations.append(sequence[:])
        permutation_found = next_permutation(sequence, lambda x, y: x < y)

    if len(permutations) == 1:
        return ''

    for perm in permutations:
        perm = "".join(perm)
        if "".join(perm) > string:
            return perm


def next_permutation(sequence, compare) -> bool:
    count = len(sequence)
    i = count

    while True:
        if i < 2:
            return False
        i -= 1
        if compare(sequence[i - 1], sequence[i]):
            break

    j = count
    while j > i and not compare(sequence[i - 1], sequence[j - 1]):
        j -= 1
    sequence[i - 1], sequence[j - 1] = sequence[j - 1], sequence[i - 1]

    j = count
    while i < j - 1:
        j -= 1
        sequence[i], sequence[j] = sequence[j], sequence[i]
        i += 1
    return True

