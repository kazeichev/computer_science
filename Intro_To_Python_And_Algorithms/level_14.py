def MaximumDiscount(n, price):
    sale = 0

    if n < 3:
        return sale

    price.sort(reverse=True)
    grouped_price = list()

    while len(price) > 0:
        grouped_price.append(price[0:3])
        del price[0:3]

    for group in grouped_price:
        if len(group) == 3:
            sale += group[2]

    return sale

