def ConquestCampaign(n, m, l, battalion):
    days = 1
    init_battalion_cords = list(set(to_pairs(battalion)))
    empty_territory = list(set(get_full_territory_cords(n, m)) - set(init_battalion_cords))
    prev_territory = init_battalion_cords

    while len(empty_territory) > 0:
        new_territories = list()

        for cords in prev_territory:
            new_territories.extend(generate_new_cords(cords, n, m))

        prev_territory.extend(new_territories)
        empty_territory = list(set(empty_territory) - set(prev_territory))
        days += 1

    return days


def get_full_territory_cords(n, m):
    cords = list()

    for n_el in range(1, n + 1):
        for m_el in range(1, m + 1):
            cords.append((n_el, m_el))

    return cords


def to_pairs(array):
    pairs = list()

    while array:
        a = array.pop(0)
        b = array.pop(0)
        pairs.append((a, b))

    return pairs


def generate_new_cords(current_cords, n, m):
    new_cords = list()

    if current_cords[1] + 1 <= m:
        new_cords.append((current_cords[0], current_cords[1] + 1))

    if 1 <= current_cords[1] - 1:
        new_cords.append((current_cords[0], current_cords[1] - 1))

    if current_cords[0] + 1 <= n:
        new_cords.append((current_cords[0] + 1, current_cords[1]))

    if 1 <= current_cords[0] - 1:
        new_cords.append((current_cords[0] - 1, current_cords[1]))

    return new_cords
