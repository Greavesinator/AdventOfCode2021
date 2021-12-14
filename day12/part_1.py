
import time
from typing import NamedTuple

input_data = open("day12/input_data.txt", 'r')


class Cave:
    def __init__(self, isLarge, id) -> None:
        self.id = id
        self.large = isLarge
        self.connections = []

    def addConnection(self, cave):
        self.connections.append(cave)


class CaveSystem:
    def __init__(self, input) -> None:
        self.caves = {}

        for line in input:
            line = line.strip()
            entry, exit = line.split("-")

            if not entry in self.caves:
                self.caves[entry] = Cave(not any(c.islower()
                                         for c in entry), entry)
            if not exit in self.caves:
                self.caves[exit] = Cave(not any(c.islower()
                                        for c in exit), exit)

            self.caves[entry].addConnection(self.caves[exit])
            self.caves[exit].addConnection(self.caves[entry])

    def findAllPaths(self):
        start = self.caves['start']
        end = self.caves['end']
        found_paths = []

        curr_path = []
        # Recursively find all paths and set found_paths
        self.nextRoute(end, start, curr_path, found_paths)
        return found_paths

    def nextRoute(self, end, cave, curr_path, found_paths):
        curr_path.append(cave.id)
        for c in cave.connections:
            if not c.large and c.id in curr_path:
                continue
            if c == end:
                curr_path.append(c.id)
                if curr_path not in found_paths:
                    found_paths.append(list(curr_path))
                curr_path.pop()
                continue
            end_found = self.nextRoute(end, c, curr_path, found_paths)
            if end_found:
                return True
        curr_path.pop()
        return False


start = time.perf_counter_ns()

c = CaveSystem(input_data.readlines())

paths = c.findAllPaths()

end = time.perf_counter_ns()

for p in c.findAllPaths():
    print(p)
print(len(paths))

print("Time elapsed: ", (end - start)/1000000.0, "ms")
