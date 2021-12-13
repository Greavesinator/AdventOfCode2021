
import time
from typing import NamedTuple

input_data = open("day10/input_data.txt", 'r')

start = time.perf_counter()

chunk_openers = ['{', '[', '<', '(']
chunk_closers = ['}', ']', '>', ')']
chunk_score = [1197, 57, 25137, 3]
error_list = []

for line in input_data.readlines():
    syntax_list = []
    for c in line:
        if c in chunk_openers:
            syntax_list.append(c)
        elif c in chunk_closers:
            if chunk_closers[chunk_openers.index(syntax_list[-1])] == c:
                syntax_list.pop()
            else:
                error_list.append(c)
                break

score = 0
for err_c in error_list:
    score += chunk_score[chunk_closers.index(err_c)]

end = time.perf_counter()

print(error_list)
print(score)

print("Time elapsed: ", (end - start)*1000.0, "us")
