import math

knots = [(0, 0)] * 10
visited = {(0, 0)}
move = {"R": (0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0)}

with open("data9.txt", "r") as f:
    for line in f:
        direction, distance = line.split(" ")
        m = move[direction]
        for _ in range(int(distance)):
            knots[0] = (knots[0][0] + m[0], knots[0][1] + m[1])

            for i in range(1, len(knots)):
                dx = knots[i-1][0] - knots[i][0]
                dy = knots[i-1][1] - knots[i][1]

                if abs(dx) > 1 or abs(dy) > 1:
                    newx, newy = knots[i][0], knots[i][1]
                    if dx:
                        newx = knots[i][0] + math.copysign(1, dx)
                    if dy:
                        newy = knots[i][1] + math.copysign(1, dy)

                    knots[i] = (newx, newy)

            visited.add(knots[-1])

print(f"Part 2: {len(visited)}")
