def Keymaker(k):
    doors = ["0"] * k
    doors[::3] = map("{}".format, ["1"] * ((k - 1) // 3 + 1))
    return "".join(doors)
