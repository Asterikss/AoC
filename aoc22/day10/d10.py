cycle = 0
cycle_table = [20 + 40 * x for x in range(6)]
cycle_values = []
x = 1

with open("data10.txt", "r") as f:
  for line in f:
    value = 0
    if line.find("noop") == -1:
      command, value = line.split(" ")
    else:
      command = "noop"
    cycle += 1

    if cycle in cycle_table:
      cycle_values.append(x * cycle)

    if command != "noop":
      cycle += 1

      if cycle in cycle_table:
        cycle_values.append(x * cycle)
      x += int(value)


print(f"Part 1: {sum(cycle_values)}")
