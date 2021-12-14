
import time


input_data = open("day8/input_data.txt", 'r')

one = 2
four = 4
seven = 3
eight = 7

hit_count = 0

start = time.perf_counter_ns()

for line in input_data.readlines():
    four_digit_string = line.split(' | ')[1]
    for digit in four_digit_string.split():
        if len(digit) == one or \
                len(digit) == four or \
                len(digit) == seven or \
                len(digit) == eight:
            hit_count += 1

end = time.perf_counter_ns()

print(hit_count)
print("Time elapsed: ", (end - start)/1000000.0, "ms")
