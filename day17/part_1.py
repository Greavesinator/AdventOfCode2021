
import time

input_data = open("day16/input_data.txt", 'r')

start = time.perf_counter_ns()


def in_target_area(x, y, targ_x_min, targ_x_max, targ_y_min, targ_y_max):
    return (x >= targ_x_min and x <= targ_x_max and y >= targ_y_min and y <= targ_y_max)


class Probe:
    def __init__(self, x_acc, y_acc) -> None:
        self.x = 0
        self.y = 0
        self.drag = 1
        self.gravity = 1
        self.x_acc = x_acc
        self.y_acc = y_acc

    def step(self):
        self.x += self.x_acc
        self.y += self.y_acc

        if 0 < self.drag:
            self.x_acc -= self.drag
        elif 0 > self.drag:
            self.x_acc += self.drag

        if self.x_acc < 0:
            self.x_acc = 0

        self.y_acc -= self.gravity


x_acc = 0
y_acc = 0
max_y = 0
for _ in range(100):
    x_acc += 1
    y_acc = 0
    for _ in range(1000):
        y_acc += 1
        target_reached = False
        p = Probe(x_acc, y_acc)
        count = 0
        top_y = 0
        while not target_reached and count < 1000:
            p.step()
            target_reached = in_target_area(p.x, p.y, 153, 199, -114, -75)
            if p.y > top_y:
                top_y = p.y
            if p.x > 199:
                # Will never reach
                break
            count += 1

        if target_reached:
            print(p.x, ",", p.y)
            if top_y > max_y:
                max_y = top_y

print("Max y:", max_y)
end = time.perf_counter_ns()
print("Time elapsed: ", (end - start)/1000000.0, "ms")
