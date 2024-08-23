from collections import defaultdict
from enum import Enum

# path = "./aoc22/day22/tdata22.txt"
path = "./aoc22/day22/data22.txt"

class Dir(Enum):
    Up = 3,
    Down = 1,
    Left = 2,
    Right = 0,

map = defaultdict(int) # 0 = nothing, 1 = trail, 2 = wall
current_cords = (-1, -1)
instructions = ""
current_direction = Dir.Right

with open(path, "r") as f:
    first_line = f.readline()
    starting_col = 0
    for i, filed in enumerate(first_line, 1):
        print(filed, i)
        if filed == ".":
            starting_col = i
            break
            
    print(starting_col)

    current_cords = 1, int(starting_col) # row, col


with open(path, "r") as f:
    for i, line in enumerate(f, 1):
        for j, filed in enumerate(line, 1):
            if filed == ".":
                map[i, j] = 1
            elif filed == "#":
                map[i, j] = 2


with open(path, "r") as f:
    data = f.read()
    instructions = data[data.rfind("\n", 0, -1):].strip()


print(f"{current_cords=}")
print(f"{instructions=}")
print(f"{current_direction=}")
print("************************")

def move(distance: int):
    global current_cords
    # print("-----------------------")
    print(f"Init distance {distance}")

    while distance > 0:
        # print("In move  ", current_cords, current_direction, distance)
        next_position = (-1, -1)

        match current_direction:
            case Dir.Up:
                next_position = (current_cords[0] - 1, current_cords[1])
            case Dir.Down:
                next_position = (current_cords[0] + 1, current_cords[1])
            case Dir.Left:
                next_position = (current_cords[0], current_cords[1] - 1)
            case Dir.Right:
                next_position = (current_cords[0], current_cords[1] + 1)

        next_field = map[next_position]
        if next_field == 1:
            current_cords = next_position
        elif next_field == 2:
            return
        else:
            print("trying to switch")
            switched_position = current_cords

            while map[switched_position] != 0:
                match current_direction:
                    case Dir.Up:
                        switched_position = (switched_position[0] + 1, switched_position[1])
                    case Dir.Down:
                        switched_position = (switched_position[0] - 1, switched_position[1])
                    case Dir.Left:
                        switched_position = (switched_position[0], switched_position[1] + 1)
                    case Dir.Right:
                        switched_position = (switched_position[0], switched_position[1] - 1)

            match current_direction:
                case Dir.Up:
                    switched_position = (switched_position[0] - 1, switched_position[1])
                case Dir.Down:
                    switched_position = (switched_position[0] + 1, switched_position[1])
                case Dir.Left:
                    switched_position = (switched_position[0], switched_position[1] - 1)
                case Dir.Right:
                    switched_position = (switched_position[0], switched_position[1] + 1)

            if map[switched_position] == 2:
                return
            elif map[switched_position] == 1:
                current_cords = switched_position
            else:
                print("SOMERHING WNET WORNG")

        distance -= 1


len_instr = len(instructions)

counter = 0

while counter < len_instr:
    curr_instr = instructions[counter]
    distance = 0

    if counter < len_instr -1 and (dist := curr_instr + instructions[counter+1]).isdigit():
        distance = dist
            # print("first     ", instructions[counter] + instructions[counter+1])
        counter += 1
    elif (dist := curr_instr).isdigit():
        distance = dist
            # print("second    ", instructions[counter])


    if distance:
        move(int(distance))
        # print(f"resulting cords {current_cords}")
        # print("-----------------------")
    else:
        # print("~~~~~~~")
        print(f"changing direction: {curr_instr}")
        # print(f"changing from {current_direction}")

        match current_direction:
            case Dir.Up:
                if curr_instr == "R":
                    current_direction = Dir.Right
                else:
                    current_direction = Dir.Left
            case Dir.Down:
                if curr_instr == "R":
                    current_direction = Dir.Left
                else:
                    current_direction = Dir.Right
            case Dir.Left:
                if curr_instr == "R":
                    current_direction = Dir.Up
                else:
                    current_direction = Dir.Down
            case Dir.Right:
                if curr_instr == "R":
                    current_direction = Dir.Down
                else:
                    current_direction = Dir.Up

        # print(f"changing to: {current_direction}")
        # print("~~~~~~~")


    counter += 1


print(f"Final result: {1000*current_cords[0] + 4*current_cords[1] + current_direction.value[0]}")
