
from os import X_OK
import time
from typing import NamedTuple

input_data = open("day12/input_data.txt", 'r')

class Cave:
    def __init__(self, isLarge) -> None:
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
                self.caves[entry] = Cave(not any(c.islower() for c in entry))
            if not exit in self.caves:
                self.caves[exit] = Cave(not any(c.islower() for c in exit))

            self.caves[entry].addConnection(self.caves[exit])
            self.caves[exit].addConnection(self.caves[entry])

    def findAllPaths(self):
        start = self.caves['start']
        end = self.caves['end']
        forbidden = []

        path_found = True
        while path_found:
            path_found, new_path = self.findPath(start, end, forbidden)

    def findPath(self, start, end, forbidden):
        new_path = []
        visited = []

        pos = start
        while pos != end:
            new_path.append(list(self.caves.keys())[list(self.caves.values()).index(pos)])
            if not pos.large:
                visited.append(pos)

            found_new_option = False
            for p in pos.connections:
                if p not in forbidden and p not in visited:
                    pos = p
                    found_new_option = True
                    break

            if not found_new_option:
                return False

        return True, new_path



start = time.perf_counter()

c = CaveSystem(input_data.readlines())

c.findAllPaths()

end = time.perf_counter()

print("Time elapsed: ", (end - start)*1000.0, "us")
