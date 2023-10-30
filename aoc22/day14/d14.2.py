from typing import DefaultDict

cave = DefaultDict(int)


def compute_cave_line(previous_x_y, x_y_tuple):
    p_x, p_y = previous_x_y
    x, y = x_y_tuple
    if p_x - x == 0:
        if y > p_y:
            for i in range(p_y + 1, y):
                cave[(x, i)] = 1
        else:
            for i in range(y + 1, p_y):
                cave[(x, i)] = 1
    else:
        if x > p_x:
            for i in range(p_x + 1, x):
                cave[(i, y)] = 1
        else:
            for i in range(x + 1, p_x):
                cave[(i, y)] = 1


with open("data14.txt") as f:
    for line in f:
        coords = line.strip().split(" -> ")
        previous_x_y = (0, 0)
        for i, coord in enumerate(coords):
            x, y = map(int, coord.split(","))
            cave[(x, y)] = 1
            if i != 0:
                compute_cave_line(previous_x_y, (x, y))
            previous_x_y = (x, y)


max_y = max(cave, key=lambda x: x[1])[1]

sand_source = (500, 0)
n_tired_sand = 0
source_blocked = False
next_one = False
s_x, s_y = sand_source

while not source_blocked:
    if next_one:
        s_x, s_y = sand_source
        next_one = False

    if cave[(s_x, s_y + 1)] == 0 and s_y + 1 != max_y + 2:
        s_y += 1

    elif cave[(s_x - 1, s_y + 1)] == 0 and s_y + 1 != max_y + 2:
        s_x -= 1
        s_y += 1

    elif cave[(s_x + 1, s_y + 1)] == 0 and s_y + 1 != max_y + 2:
        s_x += 1
        s_y += 1

    else:
        cave[(s_x, s_y)] = 2
        next_one = True
        n_tired_sand += 1
        if (s_x, s_y) == sand_source:
            source_blocked = True


print(f"Part 2:{n_tired_sand}")
