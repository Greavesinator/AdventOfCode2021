
import time


input_data = open("day8/input_data.txt", 'r')

zero = ''
one = ''
two = ''
three = ''
four = ''
five = ''
six = ''
seven = ''
eight = ''
nine = ''

hit_count = 0

start = time.perf_counter()

sum = 0

for line in input_data.readlines():
    number_dict = {}
    len_5_list = []
    len_6_list = []
    # Build our dict of simple digits.
    for digit in line.split(' | ')[0].split():
        digit = "".join(sorted(digit))
        if len(digit) == 2:
            number_dict[digit] = '1'
            one = digit
        elif len(digit) == 4:
            number_dict[digit] = '4'
            four = digit
        elif len(digit) == 3:
            number_dict[digit] = '7'
            seven = digit
        elif len(digit) == 7:
            number_dict[digit] = '8'
            eight = digit
        elif len(digit) == 5:
            # Decide if its 2,3 or 5
            len_5_list.append(digit)
        elif len(digit) == 6:
            # Decide if its 0,6,9
            len_6_list.append(digit)

        # Deduce awkward chars.
    for code in len_6_list:
        code = "".join(sorted(code))
        if len(''.join(set(code).intersection(one))) == 1:
            number_dict[code] = '6'
            six = code
        elif len(''.join(set(code).intersection(four))) == 3:
            number_dict[code] = '0'
            zero = code
        elif len(''.join(set(code).intersection(four))) == 4:
            number_dict[code] = '9'
            nine = code
    for code in len_5_list:
        code = "".join(sorted(code))
        if len(''.join(set(code).intersection(four))) == 2:
            number_dict[code] = '2'
            two = code
        else:
            if len(''.join(set(code).intersection(six))) == 4:
                number_dict[code] = '3'
                three = code
            elif len(''.join(set(code).intersection(six))) == 5:
                number_dict[code] = '5'
                five = code

    # Parse output.
    curr_result = ''
    four_digit_string = line.split(' | ')[1]
    for code in four_digit_string.split():
        code = "".join(sorted(code))
        curr_result += number_dict[code]

    print(curr_result)
    sum += int(curr_result)

end = time.perf_counter()

print(sum)
print("Time elapsed: ", (end - start)*1000.0, "us")
