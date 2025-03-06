with open("data3.txt") as f:
  all_lines = f.readlines()
  char_found = ""
  final_score = 0

  for i in range(0, len(all_lines), 3):
    print(i)

    line1 = all_lines[i].strip()
    line2 = all_lines[i + 1].strip()
    line3 = all_lines[i + 2].strip()

    for char in line1:
      if char in line2:
        if char in line3:
          char_found = char

    # if char_found.islower():
    if char_found == char_found.lower():
      print(ord(char_found) - 96)
      final_score += ord(char_found) - 96
    else:
      print(ord(char_found) - 64 + 26)
      final_score += ord(char_found) - 64 + 26

print(f"Part 2: {final_score}")
