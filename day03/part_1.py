
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
        if self.zero_count >= self.one_count:
            return 1
        else:
            return 0


input_data = open('input_data.txt', 'r')

bitArray = []

number_of_bits = 12

for i in range(number_of_bits):
    bitArray.append(BitCount())

for line in input_data:
    number = int(line, 2)
    for i in range(number_of_bits):
        bitArray[i].test_bit(number & 0x01)
        number >>= 1

gamma = 0
epsilon = 0
for i in range(number_of_bits):
    print("Ones = ", bitArray[i].one_count)
    print("Zero = ", bitArray[i].zero_count)

    gamma |= ((bitArray[i].most_common()) << i)
    epsilon |= ((bitArray[i].least_common()) << i)

print("Gamma = \t\t", bin(gamma))
print("Epsilon = \t\t", bin(epsilon))
print("Result = ", gamma * epsilon)
