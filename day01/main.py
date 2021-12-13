
last_value = 0
greater_than_count = 0
input_data = open("input_data.txt", "r")

last_value = int(input_data.readline())  # Set initial value.

for line in input_data:
    if int(line) > last_value:
        greater_than_count += 1
    last_value = int(line)

input_data.close()

print("Part 1 answer;")
print(greater_than_count)

input_data = open("input_data.txt", "r")

sliding_average_q1 = list()
sliding_average_q2 = list()

# Handle first value.
last_element = int(input_data.readline())
sliding_average_q1.insert(0, last_element)
greater_than_count = 0

for line in input_data:
    # Clear last element if full.
    if len(sliding_average_q1) >= 3:
        sliding_average_q1.pop()
    if len(sliding_average_q2) >= 3:
        sliding_average_q2.pop()

    sliding_average_q2.insert(0, last_element)
    last_element = int(line)
    sliding_average_q1.insert(0, last_element)

    # Q2 full indicates we can calculate averages.
    if len(sliding_average_q2) >= 3:
        q1_avg = sum(sliding_average_q1)
        q2_avg = sum(sliding_average_q2)

        if q1_avg > q2_avg:
            greater_than_count += 1

input_data.close()

print("Part 2 answer;")
print(greater_than_count)
