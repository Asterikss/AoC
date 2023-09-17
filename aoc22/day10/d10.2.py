cycle = 0
cycle_table = [x * 40 + 1 for x in range(1, 8)]
subtr_table = [x * 40 for x in range(8)]
currenet_row_cycle = 0
x = 1


def print_pixel(x, cycle, currenet_row_cycle, next_row=False):
    if next_row:
        print()
    if (cycle - subtr_table[currenet_row_cycle] - 1) in [x - 1, x, x + 1]:
        print("#", end="")
    else:
        print(".", end="")


with open("data10.txt", "r") as f:
    for line in f:
        value = 0
        command = "noop"
        if line.find("noop") == -1:
            command, value = line.split(" ")

        cycle += 1

        if next_row := cycle in cycle_table:
            currenet_row_cycle += 1
        print_pixel(x, cycle, currenet_row_cycle, next_row)

        if command != "noop":
            cycle += 1

            if next_row := cycle in cycle_table:
                currenet_row_cycle += 1
            print_pixel(x, cycle, currenet_row_cycle, next_row)

            x += int(value)
