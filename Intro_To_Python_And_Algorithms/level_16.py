def ShopOLAP(n, items):
    items_dict = generate_items_dict(items)
    return generate_items_list(sorted(items_dict.items(), key=lambda x: x[0]))


def generate_items_dict(items):
    items_dict = dict()

    for item in items:
        split_item = item.split(" ")

        if items_dict.get(split_item[0]):
            items_dict[split_item[0]] += int(split_item[1])
        else:
            items_dict[split_item[0]] = int(split_item[1])

    return items_dict


def generate_items_list(items):
    items_list = list()

    for item in items:
        items_list.append("{} {}".format(item[0], item[1]))

    return items_list
