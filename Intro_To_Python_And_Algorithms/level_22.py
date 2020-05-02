def BalancedParentheses(n):
    return " ".join(gen(n, 0, 0, "", list()))


def gen(n, counter_open, counter_close, string, acc):
    if counter_open + counter_close == n * 2:
        acc.append(string)
        return acc

    if counter_open < n:
        gen(n, counter_open + 1, counter_close, string + '(', acc)
    if counter_close < counter_open:
        gen(n, counter_open, counter_close + 1, string + ')', acc)

    return acc

