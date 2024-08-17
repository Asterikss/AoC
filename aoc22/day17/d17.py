from collections import defaultdict

with open("tdata17.txt", "r") as f:
    input = f.read().strip()

# rocks = [
#     [(1, 0), (2, 0), (3, 0)],
#     [(1, 0), (1, 1), (1, -1), (2, 0)],
#     [(1, 0), (2, 0), (2, 1), (2, 2)],
#     [(0, 1), (0, 2), (0, 3)],
#     [(0, 1), (1, 1), (1, 0)]
# ]

# rocks = [
#     [[0, 0], [1, 0], [2, 0], [3, 0]],
#     [[0, 0], [1, 0], [1, 1], [1, -1], [2, 0]],
#     [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]],
#     [[0, 0], [0, 1], [0, 2], [0, 3]],
#     [[0, 0], [0, 1], [1, 1], [1, 0]]
# ]

# rocks = [
#     [[3, 0], [4, 0], [5, 0], [6, 0]],
#     [[3, 0], [4, 0], [4, 1], [4, -1], [5, 0]],
#     [[3, 0], [4, 0], [5, 0], [5, 1], [5, 2]],
#     [[3, 0], [3, 1], [3, 2], [3, 3]],
#     [[3, 0], [3, 1], [4, 1], [4, 0]]
# ]

rocks = [
    [[3, 0], [4, 0], [5, 0], [6, 0]],
    # [[3, 0], [4, 0], [4, 1], [4, -1], [5, 0]],
    [[3, 1], [4, 1], [4, 2], [4, 0], [5, 1]],
    [[3, 0], [4, 0], [5, 0], [5, 1], [5, 2]],
    [[3, 0], [3, 1], [3, 2], [3, 3]],
    [[3, 0], [3, 1], [4, 1], [4, 0]]
]

def move(rock, cave, move_right: bool) -> list[list[int]]:
    can_move = True
    ret_rock = rock
    if move_right:
        if not (max(k[0] for k in rock) < 7):
            can_move = False

        for k in rock:
            for c in (c for c in cave if cave[c] == 1 and c[1] == k[1]):
                if k[0] + 1 == c[0]:
                    can_move = False
                

        if can_move:
            for i in range(len(rock)):
                ret_rock[i][0] += 1

    else:
        if not (max(k[0] for k in rock) > 1):
            can_move = False

        for k in rock:
            for c in (c for c in cave if cave[c] == 1 and c[1] == k[1]):
                if k[0] - 1 == c[0]:
                    can_move = False
                
        if can_move:
            for i in range(len(rock)):
                ret_rock[i][0] -= 1

    return ret_rock



width = 7
final_hight = 0
n_rocks = 0
max_n_rocks = 2022
curr_highest = 0

cave = defaultdict(int)
for i in range(9):
    cave[(i, 0)] = 1
input_idx_max = len(input)
rock_idx_max = len(rocks)

input_idx = 0
rock_idx = 0
# can_move = True
# can_move_counter = 0
# while n_rocks != max_n_rocks:
while True:
    # direction = input[input_idx]
    # x = 3
    # y = curr_highest + 4
    y = max(k[1] for k in cave if cave[k] == 1) + 4

    rock = rocks[rock_idx]
    for i in range(len(rock)):
        rock[i][1] += y
    # cave[(x, y)] = 1
    # for r in rocks[rock_idx]:
    #     cave[r] = 1
    can_move = True
    while can_move:
    # can_move_counter = 0
    # while can_move_counter != 2:
        # print(f"AAAA {can_move_counter}")
        direction = input[input_idx]
        if n_rocks == 1:
            print(rock)
            print(direction)
        if direction == ">":
            # rock = move_right(rock, cave)
            rock = move(rock, cave, True)
            # if max(k[1] for k in cave if cave[k] == 1) < 8:

            # if max(k[0] for k in rock) < 7:
                # for i in range(len(rock)):
                    # rock[i][0] += 1

        else:
            rock = move(rock, cave, False)
        # elif direction == "<":

            # if min(k[0] for k in rock) > 1:
                # for i in range(len(rock)):
                    # rock[i][0] -= 1
        # else:
            # print("AQAAAAAAAAAAAAAAAAAAAAAAAA")

        # if can_move:
            # for i in range(len(rock)):
                # rock[i][1] -= 1

        for k in rock:
            if cave[(k[0], k[1] - 1)] == 1:
                can_move = False

                # print("INDEXKS ADD")
                # input_idx += 1
                # if input_idx == input_idx_max:
                    # input_idx = 0
                #
                # direction = input[input_idx]
                #
                # if direction == ">":
                #     # if max(k[1] for k in cave if cave[k] == 1) < 8:
                #     if max(k[0] for k in rock) < 7:
                #         for i in range(len(rock)):
                #             rock[i][0] += 1
                #
                # else:
                # # elif direction == "<":
                #     if min(k[0] for k in rock) > 1:
                #         for i in range(len(rock)):
                #             rock[i][0] -= 1
                break

        if can_move:
        # if can_move_counter != 2:
            for i in range(len(rock)):
                rock[i][1] -= 1

        # print("INDEXKS ADD")
        input_idx += 1
        if input_idx == input_idx_max:
            input_idx = 0

            
    for k in rock:
        cave[tuple(k)] = 1

    n_rocks += 1
    print(n_rocks)
    if n_rocks + 1 == max_n_rocks:
        final_hight = max(k[1] for k in cave if cave[k] == 1)
        # print(direction)
        print(rock)
        print(cave)
        print(len(cave))
        print(n_rocks)
        print(rock_idx)
        print(input_idx)
        break
        

    # can_move_counter = 0

    rock_idx += 1
    if rock_idx == rock_idx_max:
        rock_idx = 0

    # input_idx += 1
    # if input_idx == input_idx_max:
    #     input_idx = 0
    #

    # print("--------------")
    # print(rock)
    # print(cave)
    # print(len(cave))
    # print(n_rocks)
    # print(rock_idx)
    # print(input_idx)
    # print("--------------")

    # if n_rocks == 2:
        # break


print(f"Part 1: {final_hight}")
