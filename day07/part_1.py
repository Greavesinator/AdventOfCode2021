
import time


input_data = open("day7/input_data.txt", 'r')

class CrabSwarm:
    def __init__(self, swarm_str) -> None:
        self.swarm = [int(x) for x in swarm_str.split(',')]

    def align(self, pos):
        cost = 0
        for crab in self.swarm:
            cost += abs(crab - pos)
        return cost

c = CrabSwarm(input_data.readline())

start = time.perf_counter()

best_index = 0
lowest_cost = 99999999999
for i in range(len(c.swarm)):
    cost = c.align(i)
    if lowest_cost > cost:
        best_index = i
        lowest_cost = cost

end = time.perf_counter()

print(best_index)
print(lowest_cost)
print("Time elapsed: ", (end - start)*1000.0, "us")
