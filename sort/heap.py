import heapq


def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


result = heapsort([1, 3, 5, 6, 8, 2, 0, 9])
print(result)
