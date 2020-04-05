def SumOfThe(n, data):
    for i in range(0, n):
        num = data[i]
        result = 0

        for z in range(0, n):
            if z != i:
                result += data[z]

        if num == result:
            return num
