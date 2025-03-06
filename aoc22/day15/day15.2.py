#!
sensors = set()

minimal_x = 0
minimal_y = 0
# maximal_x = 20
# maximal_y = 20
maximal_x = 4_000_000
maximal_y = 4_000_000

with open("data15.txt") as f:
  input = f.readlines()

  for line in input:
    x = int(line[line.find("x=") + 2 : line.find(",")])
    y = int(line[line.find("y=") + 2 : line.find(":")])
    x_b = int(line[line.rfind("x=") + 2 : line.rfind(",")])
    y_b = int(line[line.rfind("y=") + 2 :])
    distance = abs(y - y_b) + abs(x - x_b)

    sensors.add((x, y, distance))


def check_point(x, y):
  for sx, sy, distance in sensors:
    if abs(sx - x) + abs(sy - y) <= distance:
      return False
  return True


def calc_frequency(sensors):
  for sx, sy, distance in sensors:
    for dx in range(distance + 2):
      dy = distance + 1 - dx
      for x, y in [
        (sx + dx, sy + dy),
        (sx + dx, sy - dy),
        (sx - dx, sy + dy),
        (sx - dx, sy - dy),
      ]:
        if (
          minimal_x <= x <= maximal_x
          and minimal_y <= y <= maximal_y
          and check_point(x, y)
        ):
          print(x, y)
          return x * 4_000_000 + y


answer = calc_frequency(sensors)

print(f"Part 2: {answer}")
