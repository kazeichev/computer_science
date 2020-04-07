def UFO(n, data, octal):
    result = list()

    for i in data:
        if octal:
            num = int(str(i), 8)
        else:
            num = int(str(i), 16)

        result.append(num)

    return result
