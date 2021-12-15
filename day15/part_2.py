
import time
import re
from collections import Counter

input_data = open("day14/input_data.txt", 'r')


class Rule:
    def __init__(self, pair, middle) -> None:
        self.pair = pair
        self.middle = middle


def apply_rules(polymer, rules, loops):
    pair_dict = Counter()
    char_count = Counter()
    poly_list = []
    poly_list[:0] = polymer

    # Init pair counter
    for i in range(len(polymer)-1):
        pair = polymer[i] + polymer[i+1]
        if pair in rules:
            pair_dict[pair] += 1
        char_count[polymer[i]] += 1

    char_count[polymer[-1]] += 1

    for _ in range(loops):
        for (i, j), v in pair_dict.copy().items():
            pair_dict[i+j] -= 1*v
            pair_dict[i+rules[i+j]] += 1*v
            pair_dict[rules[i+j]+j] += 1*v
            char_count[rules[i+j]] += 1*v

    return char_count

    # new_polymer = ""
    # for i in range(len(polymer)-1):
    #     new_polymer += polymer[i]
    #     pair = polymer[i] + polymer[i+1]
    #     if pair in rules:
    #         new_polymer += rules[pair]
    # new_polymer += polymer[-1]
    # return new_polymer


def maxMin(char_count):
    common = char_count.most_common()

    max = common[0][1]
    min = common[-1][1]

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

char_count = apply_rules(polymer, rules, 40)
max, min = maxMin(char_count)

end = time.perf_counter_ns()

print(char_count)
print(max)
print(min)

print(max - min)

print("Time elapsed: ", (end - start)/1000000.0, "ms")
