def minimumWaitingTime(queries):
    queries.sort()
    totalWaitingTime = 0
    for i in range(1, len(queries)):
        totalWaitingTime += sum(queries[0:i])
    return totalWaitingTime