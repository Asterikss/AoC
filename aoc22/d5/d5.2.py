def calc_stack_nr(char_counter: int):
  return char_counter / 4 + 1


with open("data5.txt") as f:
  crates_done = False
  future_stacks_dict = dict()
  stacks = []

  for line in f:
    if not crates_done:
      char_counter = 0

      for i in range(len(line)):  # Could just do every 4
        if line[i] == "1":
          crates_done = True
          next(f, None)

          stacks = [
            future_stacks_dict[i][::-1] for i in range(1, len(future_stacks_dict) + 1)
          ]

        if line[i] == "[":
          stack_nr = calc_stack_nr(char_counter)

          if stack_nr in future_stacks_dict:
            future_stacks_dict[stack_nr].append(line[i + 1])
          else:
            future_stacks_dict[stack_nr] = [line[i + 1]]

        char_counter += 1

    else:
      start1 = line.find(" ") + 1
      end1 = line.find(" ", start1)
      how_many = int(line[start1:end1])

      start2 = line.find(" ", end1 + 1) + 1
      end2 = line.find(" ", start2)
      from_which = int(line[start2:end2]) - 1

      start3 = line.find(" ", end2 + 1) + 1
      end3 = line.find(" ", start3)
      to_which = int(line[start3:end3]) - 1

      crates_to_be_moved = stacks[from_which][-how_many:]

      for _ in range(how_many):
        stacks[from_which].pop()

      stacks[to_which].extend(crates_to_be_moved)

  print(stacks)
  final_message = ""
  for stack in stacks:
    final_message += stack[-1]

  print(f"Part 2: {final_message}")
