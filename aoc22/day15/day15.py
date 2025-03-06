#!
occupied_space = set()
beacons = set()

target_y = 2_000_000

with open("data15.txt") as f:
  for line in f:
    x = int(line[line.find("x=") + 2 : line.find(",")])
    y = int(line[line.find("y=") + 2 : line.find(":")])
    x_b = int(line[line.rfind("x=") + 2 : line.rfind(",")])
    y_b = int(line[line.rfind("y=") + 2 :])

    distance = abs(y - y_b) + abs(x - x_b)

    if (dist_to_target := abs(y - target_y)) <= distance:
      distance_left = distance - dist_to_target

      for i in range(distance_left * 2 + 1):
        occupied_space.add(x - distance_left + i)
      if y_b == target_y:
        beacons.add(x_b)

print(f"Part 1: {len(occupied_space) - len(beacons)}")
