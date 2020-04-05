def TheRabbitsFoot(string, encode):
    joined_string = string.replace(" ", "")
    n = len(joined_string)
    n_sqrt = n ** 0.5
    rows = int(n_sqrt)
    cols = int(n_sqrt + 1)

    if (rows * cols) < n:
        rows += 1

    if encode:
        return encode_string(rows, cols, joined_string)
    else:
        return decode_string(rows, string.split(" "))


def encode_string(rows, cols, string):
    matrix = list()
    encoded_result = ''

    for row in range(0, rows):
        matrix.append([])
        for col in range(0, cols):
            if len(string) > 0:
                matrix[row].append(string[0])
                string = string[1:]

    for i in range(0, rows):
        for row in matrix:
            if len(row) > i:
                encoded_result += row[i]

        encoded_result += " "

    return encoded_result.strip()


def decode_string(rows, string):
    matrix = list()
    decoded_result = ''

    i = 0
    for row in range(0, rows):
        matrix.append([])
        for str_part in string:
            if len(str_part):
                matrix[i].append(str_part[0])
                string[string.index(str_part)] = str_part[1:]

        i += 1

    for row in matrix:
        for col in row:
            decoded_result += col

    return decoded_result
