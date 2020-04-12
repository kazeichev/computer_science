def ShopOLAP(n, items):
    items_dict = generate_items_dict(n, items)
    items_for_sorting = list()

    for i in items_dict:
        items_for_sorting.append([i, items_dict[i]])

    return generate_items_list(sorted(items_for_sorting, key=lambda x: (-x[1], x[0])))


def generate_items_dict(n, items):
    items_dict = dict()

    for i in range(0, n):
        split_item = items[i].split(" ")
        if split_item[0] in items_dict:
            items_dict[split_item[0]] += int(split_item[1])
        else:
            items_dict.update({str(split_item[0]): int(split_item[1])})

    return items_dict


def generate_items_list(items):
    items_list = list()

    for item in items:
        items_list.append("{} {}".format(item[0], item[1]))

    return items_list
