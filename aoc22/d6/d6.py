with open("data6.txt") as f:
  input = f.read()

  for i in range(len(input) - 4):
    if len(set(input[i : i + 4])) == len(input[i : i + 4]):
      print(input[i : i + 4])
      print(f"Part 1: {i + 4}")
      break
