def TransformTransform(a, n):
    transformations = transform(transform(a))
    return is_key_even(generate_key(transformations))


def transform(a):
    b = list()

    for i in range(0, len(a)):
        for j in range(0, len(a) - i):
            sub = a[j:i + j + 1]
            if sub:
                b.append(max(sub))

    return b


def generate_key(transformation):
    return sum(transformation)


def is_key_even(key):
    return key % 2 == 0 if True else False
