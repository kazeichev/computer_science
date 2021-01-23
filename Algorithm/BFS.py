# Поиск в ширину (O (V + E) - кол-во вершин + кол-во рёбер)
from collections import deque

graph = {
    'you': ['alice', 'bob', 'claire'],
    'alice': ['peggy'],
    'bob': ['anuj', 'peggy'],
    'claire': ['thom', 'jonny'],
    'thom': [],
    'jonny': [],
    'peggy': [],
    'anuj': [],
}

sellers = ['claire', 'peggy']


def is_seller(name):
    return name in sellers


def find_nearest_seller():
    searched = []
    search_deque = deque(graph['you'])

    while search_deque:
        person = search_deque.popleft()

        if person not in searched:
            if is_seller(person):
                return person
            else:
                search_deque += graph[person]
                searched.append(person)

    return None

