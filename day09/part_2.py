
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
        self.basins = []

        for i, line in enumerate(map_strs):
            self.map.append([])
            for c in line:
                if c != '\n':
                    self.map[i].append(MapPoint(int(c)))

    def fetchBasins(self):
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
                    v = point.value

                    # Assess basins
                    points = [[x, y]]
                    size = 0
                    for p in points:
                        # Add points if they are greater and not 9 to keep this loop running
                        p_x = p[0]
                        p_y = p[1]

                        point = self.map[p_y][p_x]

                        if point.value != 9:
                            size += 1

                            if p_y != 0:
                                point_n = self.map[p_y - 1][p_x]
                                if point.value < point_n.value:
                                    add_p = [p_x, p_y-1]
                                    if add_p not in points:
                                        points.append(add_p)

                            if p_x != (len(self.map[p_y]) - 1):
                                point_e = self.map[p_y][p_x + 1]
                                if point.value < point_e.value:
                                    add_p = [p_x + 1, p_y]
                                    if add_p not in points:
                                        points.append(add_p)

                            if p_y != (len(self.map) - 1):
                                point_s = self.map[p_y + 1][p_x]
                                if point.value < point_s.value:
                                    add_p = [p_x, p_y+1]
                                    if add_p not in points:
                                        points.append(add_p)

                            if p_x != 0:
                                point_w = self.map[p_y][p_x - 1]
                                if point.value < point_w.value:
                                    add_p = [p_x - 1, p_y]
                                    if add_p not in points:
                                        points.append(add_p)

                    # if len(self.basins) != 3:
                    self.basins.append(size)
                    # else:
                    #     for i in range(len(self.basins)):
                    #         if self.basins[i][1] < size:
                    #             self.basins[i] = [v, size]
                    #             break

        return self.basins


input_data = open("day9/input_data.txt", 'r')

start = time.perf_counter_ns()

m = Map(input_data.readlines())

basins = m.fetchBasins()
basins.sort(reverse=True)

product = 1
for i in range(0, 3):
    product *= basins[i]

end = time.perf_counter_ns()
print(basins)
print(product)

print("Time elapsed: ", (end - start)/1000000.0, "ms")
