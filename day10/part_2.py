
import time
from typing import NamedTuple

input_data = open("day10/input_data.txt", 'r')

start = time.perf_counter()

chunk_openers = ['{', '[', '<', '(']
chunk_closers = ['}', ']', '>', ')']
chunk_score = [3, 2, 4, 1]
error_list = []
score_list = []

for line in input_data.readlines():
    syntax_list = []
    error = False
    for c in line:
        if c in chunk_openers:
            syntax_list.append(c)
        elif c in chunk_closers:
            if chunk_closers[chunk_openers.index(syntax_list[-1])] == c:
                syntax_list.pop()
            else:
                error_list.append(c)
                error = True
                break

    if not error:
        complete_string = ''
        # If we get here, remaining list is unclosed brackets.
        for c in syntax_list:
            complete_string = chunk_closers[chunk_openers.index(
                c)] + complete_string

        score = 0
        for c in complete_string:
            score *= 5
            score += chunk_score[chunk_closers.index(c)]
        score_list.append(score)

score_list.sort()
end = time.perf_counter()

print(error_list)
print(score_list)
print(score_list[int(len(score_list)/2)])

print("Time elapsed: ", (end - start)*1000.0, "us")
