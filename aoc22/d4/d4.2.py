with open("data4.txt") as f:
  counter = 0

  for line in f:
    first_first = int(line[0 : line.find("-")])
    first_second = int(line[line.find("-") + 1 : line.find(",")])

    second_first = int(line[line.find(",") + 1 : line.find("-", line.find(","))])
    second_second = int(line[line.find("-", line.find(",")) + 1 : line.find("\n")])

    added = False

    if first_first <= second_first:
      if first_second >= second_first:
        counter += 1
        added = True

    if second_first <= first_first and not added:
      if second_second >= first_first:
        counter += 1


print(f"Part 2: {counter}")
