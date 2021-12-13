
class SubmarineControls:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def forward(self, x):
        self.horizontal += x
        self.depth += (x * self.aim)

    def down(self, x):
        self.aim += x

    def up(self, x):
        self.aim -= x

    def command(self, c, x):
        if c == 'f':
            self.forward(x)
        elif c == 'd':
            self.down(x)
        elif c == 'u':
            self.up(x)


input_data = open('input_data.txt', 'r')

sub = SubmarineControls()

for line in input_data:
    sub.command(line[0], int(line.split(' ')[1]))

print("Depth = ", sub.depth)
print("Horizontal = ", sub.horizontal)

print("Product = ", (sub.depth * sub.horizontal))
