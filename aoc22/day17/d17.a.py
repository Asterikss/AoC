import copy

with open("data17.txt", "r") as f:
  input = f.read().strip()


rocks = (
  ([3, 0], [4, 0], [5, 0], [6, 0]),
  ([3, 1], [4, 1], [4, 2], [4, 0], [5, 1]),
  ([3, 0], [4, 0], [5, 0], [5, 1], [5, 2]),
  ([3, 0], [3, 1], [3, 2], [3, 3]),
  ([3, 0], [3, 1], [4, 1], [4, 0]),
)


def move(rock, move_right: bool) -> list[list[int]]:
  can_move = True
  ret_rock = rock
  if move_right:
    if not (max(k[0] for k in rock) < 7):
      can_move = False

    elif any((k[0] + 1, k[1]) in cave for k in rock):
      can_move = False

    if can_move:
      for i in range(len(rock)):
        ret_rock[i][0] += 1

  else:
    if not (min(k[0] for k in rock) > 1):
      can_move = False

    elif any((k[0] - 1, k[1]) in cave for k in rock):
      can_move = False

    if can_move:
      for i in range(len(rock)):
        ret_rock[i][0] -= 1

  return ret_rock


# def clean(max, min):
#     start = min
#     while True:
#         clean = True
#         for i in range(1, 8):
#             if (i, start) not in cave:
#                 clean = False
#
#         if clean:
#             for i in range(1, 8):
#                 del cave[(i, start)]
#
#
#         start += 1
#         if start > max:
#             break

width = 7
final_hight = 0
n_rocks = 0
max_n_rocks = 2022
curr_highest = 0

# cave = defaultdict(int)
cave = dict()
for i in range(9):
  cave[(i, 0)] = 1
input_idx_max = len(input)
rock_idx_max = len(rocks)

input_idx = 0
rock_idx = 0
# can_move = True
# can_move_counter = 0
# while n_rocks != max_n_rocks:
y_add = 4
y = 0
while True:
  # direction = input[input_idx]
  # x = 3
  # y = curr_highest + 4
  # y = max(k[1] for k in cave if cave[k] == 1) + 4
  ##CHange

  # rock = list(rocks[rock_idx])
  # rock = rocks[rock_idx]
  rock = copy.deepcopy(rocks[rock_idx])
  # print(rock)
  # print(rocks[0])
  # rock[0][0] += 9
  # print(rock)
  # print(rocks)
  # break
  # rock = rocks[rock_idx][:]
  if n_rocks == 5:
    print(rock)
  for i in range(len(rock)):
    if n_rocks == 5:
      print(f"y {y}")
    rock[i][1] += y + y_add
  # cave[(x, y)] = 1
  # for r in rocks[rock_idx]:
  #     cave[r] = 1
  can_move = True
  # print(rock)
  while can_move:
    direction = input[input_idx]
    # if n_rocks == 0:
    if n_rocks == 5:
      print(rock)
      print(direction)

    if direction == ">":
      rock = move(rock, True)
    else:
      rock = move(rock, False)

    for k in rock:
      # change
      # if cave[(k[0], k[1] - 1)] == 1:
      if (k[0], k[1] - 1) in cave:
        can_move = False
        break

    if can_move:
      # if can_move_counter != 2:
      for i in range(len(rock)):
        rock[i][1] -= 1

    # print("INDEXKS ADD")
    input_idx += 1
    if input_idx == input_idx_max:
      input_idx = 0

    if n_rocks == 5:
      print(rock)
      # print(direction)

  # y = max(k[1] for k in rock) + 4
  tmp_y = max(k[1] for k in rock)
  print(f"tmpy {tmp_y}")
  y = max(y, tmp_y)
  print(f"y {y}")

  for k in rock:
    cave[tuple(k)] = 1

  n_rocks += 1
  print(f"N_rocks {n_rocks}")
  if n_rocks == max_n_rocks:
    # final_hight = max(k[1] for k in cave if cave[k] == 1)
    final_hight = y
    print("heeeeere")
    # print(direction)
    # print(rock)
    # print(cave)
    # print(len(cave))
    # print(n_rocks)
    # print(rock_idx)
    # print(input_idx)
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
  # clean(mtop = max([self.height] + [y for x, y in self.rock]) + 2

  # top = max([y] + [k[1] for k in rock]) + 2
  # for r in range(top, -1, -1):
  #     print(f"{r:5} |", end="")
  #     for c in range(1, 8):
  #         if (c, r) in cave:
  #             print("#", end="")
  #         # elif (c, r) in self.rock:
  #             # print("@", end="")
  #         else:
  #             print(" ", end="")
  #     print("|")

  # max(k[1] for k in rock), min(k[1] for k in rock))

  # if n_rocks == 6:
  # break


print(f"Part 1: {final_hight}")
