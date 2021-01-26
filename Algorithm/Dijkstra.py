graph = {
    'start': {
        'a': 6,
        'b': 2,
    },
    'a': {
        'finish': 1,
    },
    'b': {
        'a': 3,
        'finish': 5,
    },
    'finish': {}
}

costs = {
    'a': 6,
    'b': 2,
    'finish': float('inf')
}

parents = {
    'a': 'start',
    'b': 'start',
    'finish': None,
}

processed = []


def find_lowest_cost():
    lowest_cost = float('inf')
    lowest_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_node = node

    return lowest_node


def find_way():
    node = find_lowest_cost()

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]

            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        processed.append(node)
        node = find_lowest_cost()


find_way()
print(parents)
