
import time
import re

input_data = open("day14/input_data.txt", 'r')


class Rule:
    def __init__(self, pair, middle) -> None:
        self.pair = pair
        self.middle = middle


def apply_rules(polymer, rules):
    poly_dict = {}
    poly_list = []
    poly_list[:0] = polymer

    for i in range(len(polymer)-1):
        pair = polymer[i] + polymer[i+1]
        if pair not in poly_dict:
            poly_dict[pair] = []
        poly_dict[pair] += [i+1]

    added_chars = 0
    for k, v in poly_dict.items():
        if k in rules:
            for i in v:
                poly_list.insert(i+added_chars, rules[k])
                added_chars += 1

    return "".join(poly_list)

    # new_polymer = ""
    # for i in range(len(polymer)-1):
    #     new_polymer += polymer[i]
    #     pair = polymer[i] + polymer[i+1]
    #     if pair in rules:
    #         new_polymer += rules[pair]
    # new_polymer += polymer[-1]
    # return new_polymer


def maxMin(polymer):
    max = 0
    min = 99999999999
    for c in set(polymer):
        count = polymer.count(c)
        if count > max:
            max = count
        elif count < min:
            min = count

    return max, min


start = time.perf_counter_ns()

polymer = ''
rules = {}

for line in input_data:
    line = line.strip()
    if ' -> ' in line:
        r = line.split(' -> ')
        rules[r[0]] = r[1]
    elif line != '':
        polymer = line

for i in range(40):
    print("Step: ", i)
    polymer = apply_rules(polymer, rules)
max, min = maxMin(polymer)

end = time.perf_counter_ns()

print(polymer)
print(max)
print(min)

print(max - min)

print("Time elapsed: ", (end - start)/1000000.0, "ms")
