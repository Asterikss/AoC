from queue import Queue
import math


class Monkey:
    def __init__(
        self,
        items: list[int],
        operation_sign: str,
        operation_intensity: str,
        test_nr: int,
        first_friend: int,
        second_friend: int,
    ) -> None:
        self.items = Queue()
        for item in items:
            self.items.put(item)
        self.operation_sign = operation_sign
        self.operation_intensity: str = operation_intensity
        self.test_nr = test_nr
        self.first_friend = first_friend
        self.second_friend = second_friend

        self.n_inspections = 0

    def calc_worry_lvl(self, init_lvl: int) -> int:
        self.n_inspections += 1
        if self.operation_sign == "+":
            if self.operation_intensity.isdigit():
                return init_lvl + int(self.operation_intensity)
            else:
                return init_lvl + init_lvl

        if self.operation_intensity.isdigit():
            return init_lvl * int(self.operation_intensity)
        else:
            return init_lvl * init_lvl

    def throws_to(self, init_lvl: int) -> tuple[int, int]:
        worry_lvl = int(self.calc_worry_lvl(init_lvl) / 3)
        if worry_lvl % self.test_nr == 0:
            return self.first_friend, worry_lvl
        return self.second_friend, worry_lvl

    def receive_item(self, item: int) -> None:
        self.items.put(item)

    def perform_shenanigans(self, monkeys):
        while self.items.empty() == False:
            item = self.items.get()
            throws_to, new_worry_lvl_item = self.throws_to(item)

            monkeys[throws_to].receive_item(new_worry_lvl_item)


with open("data11.txt", "r") as f:
    input = f.readlines()

monkeys: list[Monkey] = []

for i in range(1, len(input), 7):
    items = []
    operation_sign = ""
    operation_intensity = ""

    str_numbers = input[i][18:-1]
    items = list(map(int, str_numbers.split(", ")))

    if input[i + 1].find("*") != -1:
        operation_sign = "*"
        operation_intensity = input[i + 1][input[i + 1].find("*") + 2 : -1]
    else:
        operation_sign = "+"
        operation_intensity = input[i + 1][input[i + 1].find("+") + 2 : -1]

    test_nr = int(input[i + 2][input[i + 2].find("by ") + 3 : -1])

    first_friend = int(input[i + 3][-2:-1])

    second_friend = int(input[i + 4][-2:-1])

    monkeys.append(
        Monkey(
            items,
            operation_sign,
            operation_intensity,
            test_nr,
            first_friend,
            second_friend,
        )
    )


for _ in range(20):
    for monkey in monkeys:
        monkey.perform_shenanigans(monkeys)

print("_________")
counter = 0
for m in monkeys:
    print(counter, end=" :")
    q = m.items.queue
    for i in q:
        print(i, end=" ")
    print()
    counter += 1

print("_________")
highest = [0 for _ in range(2)]
for m in monkeys:
    if (n_inscp := m.n_inspections) > (min_val := min(highest)):
        highest[highest.index(min_val)] = n_inscp

print(highest)
print(f"Part 1: {math.prod(highest)}")
