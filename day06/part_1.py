
import time


input_data = open("day6/input_data.txt", 'r')


class FishSchool:
    def __init__(self, fish) -> None:
        # Index is days. Value is members
        self.fish_school = [0] * 7
        # New fish wait 2 days to enter normal school cycle.
        self.new_fish = [0] * 2

        self.curr_day = 0

        # Init fish school
        for f in fish:
            self.fish_school[f] += 1

    def _addFish(self):
        self.new_fish[1] += 1

    def passDay(self):
        # New fish produced.
        next_day_new = self.fish_school[self.curr_day]

        # Update new_fish queue.
        self.fish_school[self.curr_day] += self.new_fish[0]
        self.new_fish[0] = self.new_fish[1]
        self.new_fish[1] = next_day_new

        # Update day.
        self.curr_day += 1
        self.curr_day %= len(self.fish_school)

    def total(self):
        sum = 0
        for i in range(len(self.fish_school)):
            sum += self.fish_school[i]
        for i in range(len(self.new_fish)):
            sum += self.new_fish[i]

        return sum


initial_fish = []
for line in input_data.readlines():
    for s in line.split(','):
        initial_fish.append(int(s))

s = FishSchool(initial_fish)

print("Initial fish: ", s.fish_school)

start = time.perf_counter_ns()
for i in range(80):
    s.passDay()
end = time.perf_counter_ns()

print(s.total())
print("Time elapsed: ", (end - start)/1000000.0, "ms")
