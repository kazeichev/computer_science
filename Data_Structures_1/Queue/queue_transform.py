def queue_transform(q, n):
    while n > 0:
        tmp_value = q.dequeue()
        q.enqueue(tmp_value)
        n -= 1

    return q
