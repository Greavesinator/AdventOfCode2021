
import time

input_data = open("day16/input_data.txt", 'r')

start = time.perf_counter_ns()


class Packet:
    def __init__(self) -> None:
        self.version = 0
        self.id = 0
        self.num = 0
        self.subpackets = []

    def parse(self, bin_stream):
        arr = bin_stream
        index = 0
        for _ in range(3):
            self.version <<= 1
            self.version |= arr[index]
            index += 1
        for _ in range(3):
            self.id <<= 1
            self.id |= arr[index]
            index += 1

        # Number packet
        if self.id == 4:
            keep_parsing = True
            while keep_parsing:
                if not arr[index]:
                    keep_parsing = False

                index += 1
                for _ in range(4):
                    self.num <<= 1
                    self.num |= arr[index]
                    index += 1

        # Operator packet
        else:
            # Length bit
            # 11 bits are representing subpacket count.
            if arr[index]:
                index += 1
                count = 0
                for _ in range(11):
                    count <<= 1
                    count |= arr[index]
                    index += 1

                for _ in range(count):
                    p = Packet()
                    _, used_bits = p.parse(arr[index:])
                    self.subpackets.append(p)
                    index += used_bits

            # 15 bits are length in bits of subpackets.
            else:
                index += 1
                bit_count = 0
                for _ in range(15):
                    bit_count <<= 1
                    bit_count |= arr[index]
                    index += 1

                while bit_count != 0:
                    p = Packet()
                    _, used_bits = p.parse(arr[index:])
                    self.subpackets.append(p)
                    index += used_bits
                    bit_count -= used_bits

                pass

         # Remove trailing 0's
        used_bits = index
        index += (8 - (index % 8))
        return bin_stream[index:], used_bits

    def evaluate(self):
        result = 0
        # Sum
        if self.id == 0:
            result = 0
            for p in self.subpackets:
                result += p.evaluate()
        # Product
        if self.id == 1:
            result = 1
            for p in self.subpackets:
                result *= p.evaluate()
        # Min
        if self.id == 2:
            result = self.subpackets[0].evaluate()
            for p in self.subpackets[1:]:
                val = p.evaluate()
                if result > val:
                    result = val
        # Max
        if self.id == 3:
            result = self.subpackets[0].evaluate()
            for p in self.subpackets[1:]:
                val = p.evaluate()
                if result < val:
                    result = val
        # Literal
        if self.id == 4:
            result = self.num
        # Greater
        if self.id == 5:
            result = (self.subpackets[0].evaluate() >
                      self.subpackets[1].evaluate())
        # Less
        if self.id == 6:
            result = (self.subpackets[0].evaluate() <
                      self.subpackets[1].evaluate())
        # Equal
        if self.id == 7:
            result = (self.subpackets[0].evaluate()
                      == self.subpackets[1].evaluate())

        return result


def add_subversions(p, sum):
    sum += p.version
    for sp in p.subpackets:
        sum = add_subversions(sp, sum)
    return sum


def parse(hex_str):
    num = int(hex_str, 16)
    # Pad to expected length, to keep leading 0's
    expected_str_len = (4*len(hex_str)+2)
    bin_stream = [int(x)
                  for x in format(num, '#0'+str(expected_str_len)+'b')[2:]]

    sum = 0
    while len(bin_stream):
        p = Packet()
        bin_stream, _ = p.parse(bin_stream)
        sum += add_subversions(p, 0)
        print(p.evaluate())


parse(input_data.readline().strip())

end = time.perf_counter_ns()
print("Time elapsed: ", (end - start)/1000000.0, "ms")
