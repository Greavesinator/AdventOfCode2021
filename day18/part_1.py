
from functools import reduce
import time
import re

input_data = open("day18/input_data.txt", 'r')

start = time.perf_counter_ns()


# class Number:
#     def __init__(self) -> None:
#         self.pairs = []
#         self.max_depth = 0

#     def setLevel(self, arr, level, level_map, val):
#         if level > 0:
#             self.setLevel(arr[level_map[0]], level-1, level_map[1:], val)
#         else:
#             arr.append(val)

#     def newLevel(self, arr, level, level_map):
#         if level > 0:
#             self.newLevel(arr[level_map[0]], level-1, level_map[1:])
#         else:
#             arr.append([])

#     def parse(self, str):
#         curr_level = -1
#         level_map = []
#         for c in str:
#             if c == '[':
#                 if curr_level >= 0:
#                     self.newLevel(self.pairs, curr_level, level_map)
#                 level_map.append(False)
#                 curr_level += 1
#                 if curr_level > self.max_depth:
#                     self.max_depth = curr_level
#             elif c == ']':
#                 curr_level -= 1
#                 level_map.pop()
#             elif c == ',':
#                 level_map[curr_level] = True
#             elif c.isnumeric():
#                 self.setLevel(self.pairs, curr_level, level_map, int(c))
#                 pass

#     def _explode(self):
#         return False

#     def _split(self):
#         return False

#     def _reduce(self):
#         action_taken = True
#         while action_taken:
#             action_taken = False
#             # Check explode step
#             if self._explode():
#                 action_taken = True
#             elif self._split():
#                 action_taken = True

#     def __add__(self, rhs):
#         n = Number()
#         n.pairs = [self.pairs, rhs.pairs]
#         n._reduce()
#         return n


# n = Number()
# n.parse("[1,2]")
# n1 = Number()
# n1.parse("[[3,4],5]")
# print(n.pairs)
# print(n1.pairs)

# sum = n + n1
# print(sum.pairs)

def split(x):
    index = 0
    action = False

    r = re.search("[0-9][0-9]+", x[index:])
    if r is not None:
        action = True
        start, end = r.span()
        start += index
        end += index

        num = int(x[start:end])
        lhs = int(num/2)
        rhs = int((num+1)/2)

        x = x[:start] + '[' + str(lhs) + ',' + str(rhs) + ']' + x[end:]
        index = end+2  # ??

    return x, action


def explode(x):
    lhs_index = 0
    level = 0
    action = False
    result = ""
    for i, c in enumerate(x):
        if c == '[':
            level += 1
            result += c
        elif c == ']':
            level -= 1
            result += c
        elif c.isnumeric():
            if level > 4:
                r = re.search("[0-9]+,[0-9]+", x[i:])
                if r is not None:
                    start, end = r.span()
                    start += i
                    end += i
                    lhs_num, rhs_num = [int(s)
                                        for s in x[start:end].split(',')]
                    # FIX. Find last match of [0-9]+ in x[:start]
                    match = None
                    for match in re.finditer(r"[0-9]+", x[:start]):
                        pass
                    if match is not None:
                        lhs_start, lhs_end = match.span()
                        result = result[:lhs_start] + \
                            str(lhs_num +
                                int(result[lhs_start:lhs_end])) + result[lhs_end:]

                    # Get rhs and do same
                    r = re.search("[0-9]+", x[end:])
                    if r is not None:
                        rhs_start, rhs_end = r.span()
                        rhs_start += end
                        rhs_end += end
                        x = x[:rhs_start] + \
                            str(rhs_num +
                                int(x[rhs_start:rhs_end])) + x[rhs_end:]

                    # Replace pair with 0 and add rest of string.
                    result = result[:-1] + '0' + x[end + 1:]
                    action = True
                break
            lhs_index = i
            result += c
        else:
            result += c
    return result, action


def add(x, y):
    result = '[' + x + ',' + y + ']'
    while True:
        result, action = explode(result)
        if not action:
            result, action = split(result)
            if not action:
                break
    print(result)
    return result


def magnitude(x):
    while True:
        r = re.search("[0-9]+,[0-9]+", x)
        if r is not None:
            start, end = r.span()
            lhs_num, rhs_num = [int(s)
                                for s in x[start:end].split(',')]
            x = x[:start-1] + str(lhs_num*3+rhs_num*2) + x[end + 1:]
        else:
            break
    return int(x)


lines = [x.strip() for x in input_data.readlines()]
result = reduce(add, lines)

print(magnitude(result))
# print(add("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]"))
end = time.perf_counter_ns()
print("Time elapsed: ", (end - start)/1000000.0, "ms")
