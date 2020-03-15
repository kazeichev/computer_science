def odometer(driving_data):
    driving_data_pairs = to_pairs(driving_data)
    distance = 0
    prev_time = 0

    for pair in driving_data_pairs:
        distance += pair[0] * (pair[1] - prev_time)
        prev_time = pair[1]

    return distance


def to_pairs(array):
    pairs = list()

    while array:
        a = array.pop(0)
        b = array.pop(0)
        pairs.append((a, b))

    return pairs
