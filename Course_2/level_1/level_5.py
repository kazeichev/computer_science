def PatternUnlock(n, hits):
    length = 0
    result = ''

    for i in range(0, n):
        if (i + 1) < n:
            if is_vertical_or_horizontal_sibling(hits[i], hits[i + 1]):
                length += 1
            else:
                length += 1.41421

    length_list = list(str(round(length, 5)))
    for i in range(0, len(length_list)):
        if length_list[i] == '.' or length_list[i] == '0':
            continue

        result += length_list[i]

    return result


def is_vertical_or_horizontal_sibling(current_val, next_val):
    in_same_row = False
    current_val_index = 0
    next_val_index = 0
    matrix = [
        [6, 1, 9],
        [5, 2, 8],
        [4, 3, 7]
    ]

    for matrix_row in matrix:
        if current_val in matrix_row and next_val in matrix_row:
            in_same_row = True
        else:
            in_same_row = False

            for matrix_val in matrix_row:
                if matrix_val == next_val:
                    next_val_index = matrix_row.index(matrix_val)

                if matrix_val == current_val:
                    current_val_index = matrix_row.index(matrix_val)

    if in_same_row:
        return True

    if next_val_index == current_val_index:
        return True

    return False
