x = 0
y = 0
cord_set = set()
head = (x, y)
tail = (x, y)
cord_set.add(tail)

# def calc_tail_movement(new_head, tail, direction):
#     if new_head[0] == tail[0]:
#         if direction == "R":
#             return tail(tail[0], tail[1] + 1)
#         if direction == "L":
#             return tail(tail[0], tail[1] - 1)
        

def calc_movement(direction, head, tail):
    new_head = ()
    new_tail = tail
    match direction:
        case "R":
            new_head = (head[0], head[1] + 1)
            # print(f"new head {new_head}")
            if new_head[0] == tail[0] and abs(tail[1] - new_head[1]) > 1:
                new_tail = (tail[0], tail[1] + 1)

            elif new_head[0] != tail[0] and abs(tail[1] - new_head[1]) > 1:
                if new_head[0] > tail[0]:
                    new_tail = (tail[0] + 1, tail[1] + 1)
                else:
                    new_tail = (tail[0] - 1, tail[1] + 1)
            # new_tail = calc_tail_movement(new_head, tail, direction)

        case "L":
            new_head = (head[0], head[1] - 1)
            # print(f"new head {new_head}")
            if new_head[0] == tail[0] and abs(tail[1] - new_head[1]) > 1:
                new_tail = (tail[0], tail[1] - 1)

            elif new_head[0] != tail[0] and abs(tail[1] - new_head[1]) > 1:
                if new_head[0] > tail[0]:
                    new_tail = (tail[0] + 1, tail[1] - 1)
                else:
                    new_tail = (tail[0] - 1, tail[1] - 1)

        case "U":
            new_head = (head[0] + 1, head[1])
            # print(f"new head {new_head}")
            if new_head[1] == tail[1] and abs(tail[0] - new_head[0]) > 1:
                new_tail = (tail[0] + 1, tail[1])

            # to pierwsze nie jest potrzebne, drugie chyba też nie
            elif new_head[1] != tail[1] and abs(tail[0] - new_head[0]) > 1:
                if new_head[1] > tail[1]:
                    new_tail = (tail[0] + 1, tail[1] + 1)
                else:
                    new_tail = (tail[0] + 1, tail[1] - 1)

        case "D":
            new_head = (head[0] - 1, head[1])
            # print(f"new head {new_head}")
            if new_head[1] == tail[1] and abs(tail[0] - new_head[0]) > 1:
                new_tail = (tail[0] - 1, tail[1])

            # to pierwsze nie jest potrzebne, drugie chyba też nie
            elif new_head[1] != tail[1] and abs(tail[0] - new_head[0]) > 1:
                if new_head[1] > tail[1]:
                    new_tail = (tail[0] - 1, tail[1] + 1)
                else:
                    new_tail = (tail[0] - 1, tail[1] - 1)
    
    return new_head, new_tail


with open("data9.txt", "r") as f:
    for line in f:
        direction = line[0]
        distance = line[line.find(" ") + 1:-1]
        # print(distance)
        for i in range(int(distance)):
            # print(f"head: {head}")
            head, tail = calc_movement(direction, head, tail)
            cord_set.add(tail)

        # print(head)
        # print(tail)
        # print(cord_set)
        # break


    print(head)
    print(tail)
    print(cord_set)

    print(f"Part 1: {len(cord_set)}")
    
