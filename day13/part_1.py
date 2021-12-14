
import time

input_data = open("day13/input_data.txt", 'r')


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Page:
    def __init__(self, page_str) -> None:
        points = []

        self.folds = []

        largest_x = 0
        largest_y = 0

        for line in page_str:
            line = line.strip()
            if "fold" in line:
                if "y" in line:
                    self.folds.append(Point(0, int(line.split("=")[1])))
                elif "x" in line:
                    self.folds.append(Point(int(line.split("=")[1]), 0))
            elif ',' in line:
                x, y = [int(x) for x in line.split(",")]
                points.append(Point(x, y))
                if x > largest_x:
                    largest_x = x
                if y > largest_y:
                    largest_y = y

        self.contents = [[0] * (largest_x+1) for _ in range(largest_y+1)]

        for p in points:
            self.contents[p.y][p.x] = 1

    def perfFold(self):
        self.foldX(self.folds[0])

    def foldX(self, foldp):
        folded = []
        for y, row in enumerate(self.contents):
            folded.insert(y, [])
            for x, p in enumerate(row[0:int(len(row)/2)]):
                folded[y].insert(x, (p or row[len(row)-x-1]))

        self.contents = folded

    def foldY(self, foldp):
        folded = []
        for y, row in enumerate(self.contents[0:int(len(self.contents)/2)]):
            folded.insert(y, [])
            for x, p in enumerate(row):
                folded[y].insert(
                    x, (p or self.contents[len(self.contents)-y-1][x]))

        self.contents = folded

    def count(self):
        return sum(x for row in self.contents for x in row)

    def display(self):
        for row in self.contents:
            print()
            for i in row:
                print(str(i) + " ", end='')
        print()


start = time.perf_counter_ns()

p = Page(input_data.readlines())
# p.display()

p.perfFold()

# p.display()

print(p.count())

end = time.perf_counter_ns()

print("Time elapsed: ", (end - start)/1000000.0, "ms")
