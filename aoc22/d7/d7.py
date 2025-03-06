from collections import defaultdict

current_dir = ["/"]
dir_sizes = defaultdict(int)

with open("data7.txt") as f:
  next(f, None)
  for line in f:
    if line.find(" ls") == -1 and line.find("dir ") == -1:
      if line.find("cd ..") != -1 and len(current_dir) > 1:
        current_dir.pop()

      elif line.find(" cd ") != -1:
        current_dir.append(line[5 : line.find("\n")])

      else:
        if (size := line[0 : line.find(" ")]).isdigit():
          for i in range(0, len(current_dir)):
            dir_sizes["/".join(current_dir[: i + 1])] += int(size)


final_sum = sum(x for x in dir_sizes.values() if x <= 100_000)
print(f"Part 1: {final_sum}")
