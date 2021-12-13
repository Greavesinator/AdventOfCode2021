
class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def display(self):
        print("{", self.x, ", ", self.y, "}")

class SteamMap:
    def __init__(self, size) -> None:
        self.map = []
        self.size = size
        for i in range(size):
            self.map.append([])
            for x in range(size):
                self.map[i].append(0)

    def markLine(self, start, end):
        if start.x == end.x:
            if start.y > end.y:
                r = range(end.y, start.y + 1)
            else:
                r = range(start.y, end.y + 1)
            for i in r:
                self.map[i][start.x] += 1

        elif start.y == end.y:
            if start.x > end.x:
                r = range(end.x, start.x + 1)
            else:
                r = range(start.x, end.x + 1)
            for i in r:
                self.map[start.y][i] += 1

        else:
            # Only true diagonals allowed.
            if start.y > end.y:
                y_r = list(range(start.y, end.y - 1, -1))
            else:
                y_r = list(range(start.y, end.y + 1))

            if start.x > end.x:
                x_r = list(range(start.x, end.x -1, -1))
            else:
                x_r = list(range(start.x, end.x + 1))

            for i in range(len(y_r)):
                self.map[y_r[i]][x_r[i]] += 1

    def display(self):
        print()
        for i in range(self.size):
            print()
            for j in range(self.size):
                print(self.map[i][j], end="")
        print()

    def displayOverlaps(self):
        sum = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.map[i][j] >= 2:
                    sum += 1
        print(sum)


def parse_coordinate(str):
    coord_string = str.split(" -> ")
    start = [int(x) for x in coord_string[0].split(',')]
    end = [int(x) for x in coord_string[1].split(',')]
    return Coordinate(start[0], start[1]), Coordinate(end[0], end[1])

map = SteamMap(1000)

input_data = open("day5/input_data.txt", 'r')
for line in input_data.readlines():
    start, end = parse_coordinate(line)
    map.markLine(start, end)

# map.display()
map.displayOverlaps()
