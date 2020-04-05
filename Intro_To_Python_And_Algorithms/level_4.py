def SynchronizingTables(n, ids, salary):
    copied_ids = ids.copy()
    salary_handbook = {}
    result = list()

    copied_ids.sort()
    salary.sort()

    for i in range(0, n):
        salary_handbook[copied_ids[i]] = salary[i]

    for id in ids:
        result.append(salary_handbook[id])

    return result
