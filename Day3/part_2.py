
class BitCount:
    def __init__(self):
        self.one_count = 0
        self.zero_count = 0

    def test_bit(self, x):
        if x:
            self.one_count += 1
        else:
            self.zero_count += 1

    def most_common(self):
        if self.one_count >= self.zero_count:
            return 1
        else:
            return 0

    def least_common(self):
        if self.zero_count > self.one_count:
            return 1
        else:
            return 0


input_data = open('input_data.txt', 'r')

bitArray = []

dataset = []

number_of_bits = 12

for line in input_data:
    number = int(line, 2)
    dataset.append(number)

oxygen = list(dataset)
carbon_dioxide = list(dataset)

for i in reversed(range(number_of_bits)):
    if(len(dataset) == 1):
        break

    bit_count = BitCount()
    [bit_count.test_bit((x >> i) & 0x1) for x in oxygen]

    if len(oxygen) != 1:
        for number in list(oxygen):
            if((number >> i) & 0x1) != bit_count.most_common():
                oxygen.remove(number)
    print("oxygen = ", oxygen)

    bit_count = BitCount()
    [bit_count.test_bit((x >> i) & 0x1) for x in carbon_dioxide]

    if len(carbon_dioxide) != 1:
        for number in list(carbon_dioxide):
            if((number >> i) & 0x1) != bit_count.least_common():
                carbon_dioxide.remove(number)

print([bin(number) for number in oxygen])
print([bin(number) for number in carbon_dioxide])
print("Product = ", (oxygen[0] * carbon_dioxide[0]))
