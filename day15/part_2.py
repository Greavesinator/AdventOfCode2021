
import time
from queue import PriorityQueue

input_data = open("day15/input_data.txt", 'r')


class Graph:
    def __init__(self, num):
        self.v = num
        self.visited = set()
        self.edges = [[-1 for i in range(num)]
                      for j in range(num)]

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight


def dijkstra(graph):
    D = {v: float('inf') for v in range(graph.v*graph.v)}
    start = (0, 0)
    end = (graph.v-1, graph.v-1)
    D[start[1]*graph.v + start[0]] = 0

    pq = PriorityQueue()
    pq.put((0, start[0], start[1]))

    while not pq.empty():
        (cost, x, y) = pq.get()
        graph.visited.add((x, y))

        if end == (x, y):
            return D

        neighbours = []

        if y != 0:
            neighbours.append((x, y-1))

        if x != (len(graph.edges[y]) - 1):
            neighbours.append((x+1, y))

        if y != (len(graph.edges) - 1):
            neighbours.append((x, y+1))

        if x != 0:
            neighbours.append((x-1, y))

        for p in neighbours:
            if p not in graph.visited:
                old_cost = D[p[1]*graph.v + p[0]]
                new_cost = cost + graph.edges[p[1]][p[0]]
                if new_cost < old_cost:
                    pq.put((new_cost, p[0], p[1]))
                    D[p[1]*graph.v + p[0]] = new_cost

    return D


start = time.perf_counter_ns()

data = []

for i, line in enumerate(input_data):
    line = line.strip()
    data.append(list(map(int, line)))

w = len(data)
h = len(data[0])

for _ in range(4):
    for row in data:
        tail = row[-w:]
        row.extend((x + 1) if x < 9 else 1 for x in tail)

for _ in range(4):
    for row in data[-h:]:
        row = [(x + 1) if x < 9 else 1 for x in row]
        data.append(row)

g = Graph(len(data))

end = time.perf_counter_ns()
print("Time elapsed: ", (end - start)/1000000.0, "ms")

for i, row in enumerate(data):
    for j, cost in enumerate(row):
        # From 0 -> 1 costs 4
        g.add_edge(i, j, data[i][j])

end = time.perf_counter_ns()
print("Time elapsed: ", (end - start)/1000000.0, "ms")

D = dijkstra(g)

end = time.perf_counter_ns()

print(D[g.v*g.v - 1])

print("Time elapsed: ", (end - start)/1000000.0, "ms")
