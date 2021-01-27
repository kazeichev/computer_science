# Жадные алгоритмы

# Поиск оптимального кол-ва радиостанций для покрытия всех штатов - O(n^2)

# Найти станцию, покрывающую наибольшее кол-во штатов -> добавить станцию в результирующий список ->
# убрать штаты из списка -> повторить пока штаты не закончаться

states = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {
    'kone': set(['id', 'nv', 'ut']),
    'ktwo': set(['wa', 'id', 'mt']),
    'kthree': set(['or', 'nv', 'ca']),
    'kfour': set(['nv', 'ut']),
    'kfive': set(['ca', 'az']),
}

best_stations = set()
while states:
    best_station = None
    covered_states = set()

    for station, states_of_station in stations.items():
        covered = states & states_of_station
        if len(covered) > len(covered_states):
            covered_states = covered
            best_station = station

    states -= covered_states
    best_stations.add(best_station)

print(best_stations)
