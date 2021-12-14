
from os import X_OK
import time
from typing import NamedTuple

input_data = open("day11/input_data.txt", 'r')


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def get_diagonals(p, list_2d):
    diag_elems = []
    x = p.x
    y = p.y
    # Assess points around this.
    if y != 0:
        point_n = Point(x, y-1)
        diag_elems.append(point_n)
        if x != 0:
            point_nw = Point(x-1, y-1)
            diag_elems.append(point_nw)

    if x != (len(list_2d[y]) - 1):
        point_e = Point(x+1, y)
        diag_elems.append(point_e)
        if y != 0:
            point_ne = Point(x+1, y-1)
            diag_elems.append(point_ne)
        if y != (len(list_2d) - 1):
            point_se = Point(x+1, y+1)
            diag_elems.append(point_se)

    if y != (len(list_2d) - 1):
        point_s = Point(x, y+1)
        diag_elems.append(point_s)
        if x != 0:
            point_sw = Point(x-1, y+1)
            diag_elems.append(point_sw)

    if x != 0:
        point_w = Point(x-1, y)
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

    def updateDiags(self, p):
        diag_points = get_diagonals(p, self.swarm)
        for p in diag_points:
            # Already going to flash, no need to continue this chain.
            # Flash will have already been handled.
            if self.swarm[p.y][p.x].willFlash():
                continue
            self.swarm[p.y][p.x].updateStep()
            if self.swarm[p.y][p.x].willFlash():
                self.updateDiags(p)

    def step(self):
        for y, row in enumerate(self.swarm):
            for x, octo in enumerate(row):
                # Already going to flash, no need to continue this chain.
                # Flash will have already been handled.
                if octo.willFlash():
                    continue
                octo.updateStep()

                if octo.willFlash():
                    self.updateDiags(Point(x, y))

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


start = time.perf_counter_ns()

s = OctoSwarm(input_data.readlines())

for i in range(100):
    s.step()

end = time.perf_counter_ns()

print(s.flash_count)

print("Time elapsed: ", (end - start)/1000000.0, "ms")
