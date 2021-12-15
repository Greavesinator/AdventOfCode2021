
import time
from queue import PriorityQueue

input_data = open("day15/input_data.txt", 'r')


class Graph:
    def __init__(self, num):
        self.v = num
        self.visited = []
        self.edges = [[-1 for i in range(num)]
                      for j in range(num)]

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight


def dijkstra(graph, start_v):
    D = {v: float('inf') for v in range(graph.v)}
    D[start_v] = 0

    pq = PriorityQueue()
    pq.put((0, start_v))

    while not pq.empty():
        (_, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


start = time.perf_counter_ns()

data = []

for i, line in enumerate(input_data):
    line = line.strip()
    data.append([])
    for j, cost in enumerate(line):
        data[i].append(int(cost))

g = Graph(len(data)*len(data[0]))

for i, row in enumerate(data):
    for j, cost in enumerate(row):
        # From 0 -> 1 costs 4
        id = i*len(data) + j
        if j != (len(row) - 1):
            id_e = id + 1
            g.add_edge(id, id_e, row[j+1])
        if j != 0:
            id_w = id - 1
            g.add_edge(id, id_w, row[j-1])
        if i != (len(data) - 1):
            id_s = id + len(data)
            g.add_edge(id, id_s, data[i+1][j])
        if i != 0:
            id_n = id - len(data)
            g.add_edge(id, id_n, data[i-1][j])


g.add_edge(0, 0, 0)
D = dijkstra(g, 0)

end = time.perf_counter_ns()

for vertex in range(len(D)):
    print("0 -> ", vertex, "is", D[vertex])

print("Time elapsed: ", (end - start)/1000000.0, "ms")
