# Only works for smaller input (example input)
occupied_space = set()
beacons = set()
sensors = set()

minimal_x = 0
minimal_y = 0
maximal_x = 20
maximal_y = 20
current_y = 0

answer = 0

helper_table = [i for i in range(minimal_x, maximal_x + 1)]
helper_table_len = len(helper_table)

with open("tdata15.txt") as f:
    input = f.readlines()

    while True:
        for line in input:
            x = int(line[line.find("x=") + 2 : line.find(",")])
            y = int(line[line.find("y=") + 2 : line.find(":")])
            x_b = int(line[line.rfind("x=") + 2 : line.rfind(",")])
            y_b = int(line[line.rfind("y=") + 2 :])

            distance = abs(y - y_b) + abs(x - x_b)

            if (dist_to_target := abs(y - current_y)) <= distance:
                distance_left = distance - dist_to_target
                for i in range(distance_left * 2 + 1):
                    occupied_space.add(x - distance_left + i)
                if y_b == current_y:
                    beacons.add(x_b)
                if y == current_y:
                    sensors.add(x)

        tmp_a = [x for x in occupied_space if x in helper_table]

        if len(tmp_a) < helper_table_len:
            tmp_b = [x for x in helper_table if x not in tmp_a]
            answer = int(tmp_b[0]) * 4_000_000 + current_y
            break

        occupied_space.clear()
        beacons.clear()
        sensors.clear()

        current_y += 1


print(f"Part 2: {answer}")
