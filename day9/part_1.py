
import time

class MapPoint:
    def __init__(self, value) -> None:
        self.value = value

        self.north = False
        self.east = False
        self.south = False
        self.west = False
        pass
    def isLowPoint(self):
        return self.north and self.east and self.south and self.west

class Map:
    def __init__(self, map_strs) -> None:
        self.map = []

        for i, line in enumerate(map_strs):
            self.map.append([])
            for c in line:
                if c != '\n':
                    self.map[i].append(MapPoint(int(c)))


input_data = open("day9/input_data.txt", 'r')

start = time.perf_counter()

m = Map(input_data.readlines())

end = time.perf_counter()

print("Time elapsed: ", (end - start)*1000.0, "us")
