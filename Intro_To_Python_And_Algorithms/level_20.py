def MatrixTurn(matrix, strings, columns, t):
    result_matrix = generate_empty_matrix(strings, columns)
    initial_matrix = generate_initial_matrix(matrix)

    for ring in range(0, int(min(strings, columns) / 2)):
        for i in range(ring, strings - ring):
            for j in range(ring, columns - ring):
                string_index = i
                column_index = j
                iterate = t

                while iterate > 0:
                    if string_index >= ring and string_index < strings - ring - 1 and column_index == ring:
                        string_index += 1
                    elif column_index > ring and column_index < columns - ring and string_index == ring:
                        column_index -= 1
                    elif string_index > ring and string_index < strings - ring and column_index == columns - ring - 1:
                        string_index -= 1
                    elif column_index < columns - ring - 1 and column_index >= ring and string_index == strings - ring - 1:
                        column_index += 1

                    result_matrix[i][j] = initial_matrix[string_index][column_index]
                    iterate -= 1

    generate_result(matrix, result_matrix, strings, columns)
    print(matrix)


def generate_result(matrix, result_matrix, strings, columns):

    for i in range(0, strings):
        matrix[i] = ""
        for j in range(0, columns):
            matrix[i] = "".join(result_matrix[i])


def generate_initial_matrix(matrix):
    result = list()

    for i in matrix:
        result.append(list(i))

    return result


def generate_empty_matrix(s, c):
    matrix = list()

    for i in range(0, s):
        matrix.append([])
        for j in range(0, c):
            matrix[i].append([])

    return matrix
