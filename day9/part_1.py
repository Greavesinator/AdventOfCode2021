
import time


class MapPoint:
    def __init__(self, value) -> None:
        self.value = value

        self.north = True
        self.east = True
        self.south = True
        self.west = True

    def isLowPoint(self):
        return self.north and self.east and self.south and self.west


class Map:
    def __init__(self, map_strs) -> None:
        self.map = []
        self.low_points = []

        for i, line in enumerate(map_strs):
            self.map.append([])
            for c in line:
                if c != '\n':
                    self.map[i].append(MapPoint(int(c)))

    def fetchLowPoints(self):
        for y in range(len(self.map)):
            for x, point in enumerate(self.map[y]):
                # Check point is not already invalidated.
                if point.isLowPoint():
                    # Assess points around this.
                    if y != 0:
                        point_n = self.map[y - 1][x]
                        point.north = point.value < point_n.value
                        point_n.south = point_n.value < point.value

                    if x != (len(self.map[y]) - 1):
                        point_e = self.map[y][x + 1]
                        point.east = point.value < point_e.value
                        point_e.west = point_e.value < point.value

                    if y != (len(self.map) - 1):
                        point_s = self.map[y + 1][x]
                        point.south = point.value < point_s.value
                        point_s.north = point_s.value < point.value

                    if x != 0:
                        point_w = self.map[y][x - 1]
                        point.west = point.value < point_w.value
                        point_w.east = point_w.value < point.value

                if point.isLowPoint():
                    self.low_points.append(point.value)

        return self.low_points


input_data = open("day9/input_data.txt", 'r')

start = time.perf_counter()

m = Map(input_data.readlines())

lp = m.fetchLowPoints()
# Get risk (1+height)
sum = 0
for p in lp:
    sum += p+1

end = time.perf_counter()

print(lp)
print(sum)

print("Time elapsed: ", (end - start)*1000.0, "us")
