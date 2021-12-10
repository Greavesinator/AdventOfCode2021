
class BingoCard:
    class BingoNumber:
        def __init__(self, number):
            self.number = number
            self.marked = False

        def display(self):
            print("{", self.number, ", ", self.marked, "}", end="")

    def __init__(self, size):
        self.numbers = []
        self.size = size
        self.last_call = 0

    def addNumber(self, num):
        self.numbers.append(self.BingoNumber(num))

    def display(self):
        for i in range(self.size):
            for x in range(self.size):
                self.numbers[i*self.size + x].display()
            print()

    def checkNumber(self, num):
        self.last_call = num
        for item in self.numbers:
            if item.number == num:
                item.marked = True
                break

    def checkBingo(self):
        # Check rows
        for i in range(self.size):
            row_complete = True
            for x in range(self.size):
                row_complete &= self.numbers[i*self.size + x].marked

            if row_complete:
                return True

        # Check columns
        for i in range(self.size):
            col_complete = True
            for x in range(i, len(self.numbers), self.size):
                col_complete &= self.numbers[x].marked

            if col_complete:
                return True

        return False

    def getScore(self):
        sum = 0
        for num in self.numbers:
            if not num.marked:
                sum += num.number

        return sum * self.last_call

input_data = open("input_data.txt", "r")

bingo_call_list = [int(x) for x in input_data.readline().split(',')]

print("Sneak peak: ", bingo_call_list)

all_cards = []

row_size = 5

for line in input_data.readlines():
    if line == '\n':
        all_cards.append(BingoCard(row_size))
    else:
        for num in line.split():
            all_cards[-1].addNumber(int(num))

for call_num in bingo_call_list:
    for i, card in list(enumerate(all_cards)):
        card.checkNumber(call_num)

        if card.checkBingo():
            if len(all_cards) == 1:
                print("Match!")
                card.display()
                print(card.getScore())
            all_cards.remove(card)
