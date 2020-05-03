def Keymaker(k):
    doors = ["1"] * k
    iterate(doors, 1, 2, k)

    return "".join(doors)


def iterate(doors, start, step, k):
    if start == k:
        return doors

    doors[start::step] = map(lambda n: "1" if n == "0" else "0", doors[start::step])
    iterate(doors, start + 1, step + 1, k)
