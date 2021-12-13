
import time
from typing import NamedTuple

input_data = open("day11/input_data.txt", 'r')


def get_diagonals(x, y, list_2d):
    diag_elems = []
    # Assess points around this.
    if y != 0:
        point_n = list_2d[y - 1][x]
        diag_elems.append(point_n)
        if x != 0:
            point_nw = list_2d[y - 1][x - 1]
            diag_elems.append(point_nw)

    if x != (len(list_2d[y]) - 1):
        point_e = list_2d[y][x + 1]
        diag_elems.append(point_e)
        if y != 0:
            point_ne = list_2d[y - 1][x + 1]
            diag_elems.append(point_ne)
        if y != (len(list_2d) - 1):
            point_se = list_2d[y + 1][x + 1]
            diag_elems.append(point_se)

    if y != (len(list_2d) - 1):
        point_s = list_2d[y + 1][x]
        diag_elems.append(point_s)
        if x != 0:
            point_sw = list_2d[y + 1][x - 1]
            diag_elems.append(point_sw)

    if x != 0:
        point_w = list_2d[y][x - 1]
        diag_elems.append(point_w)

    return diag_elems


class Octopus:
    def __init__(self, val) -> None:
        self.value = val

    def updateStep(self):
        if self.value < 10:
            self.value += 1

    def willFlash(self):
        if self.value >= 10:
            return True
        return False

    def checkFlash(self):
        if self.value >= 10:
            self.value = 0
            return True
        return False


class OctoSwarm:
    def __init__(self, swarm_str) -> None:
        self.swarm = []
        self.flash_count = 0
        for i, line in enumerate(swarm_str):
            self.swarm.append([])
            for c in line:
                if c != '\n':
                    self.swarm[i].append(Octopus(int(c)))

    def step(self):
        for x, row in enumerate(self.swarm):
            for y, octo in enumerate(row):
                octo.updateStep()

                if octo.willFlash():
                    diag_octos = get_diagonals(x, y, self.swarm)
                    for o in diag_octos:
                        o.updateStep()

        for row in self.swarm:
            for octo in row:
                if octo.checkFlash():
                    self.flash_count += 1

    def display(self):
        for row in self.swarm:
            print()
            for octo in row:
                print(octo.value, ", ", end="")
        print()


start = time.perf_counter()

s = OctoSwarm(input_data.readlines())

print("Initial;")
s.display()

for i in range(10):
    s.step()
    print("Step ", i+1, ";")
    s.display()

end = time.perf_counter()

print(s.flash_count)

print("Time elapsed: ", (end - start)*1000.0, "us")
