def squirrel(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return str(fact)[0]
