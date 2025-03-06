# A Rock B Paper C Scissors
# X lose Y draw Z win
# Rock - 1 Paper - 2 Scissors - 3
# lost - 0, drew - 3, won- 6

final_score = 0


def calc_output(opp_choice: str, strategy: str) -> int:
  match strategy:
    case "X":
      match opp_choice:
        case "A":
          return 3  # Scissors
        case "B":
          return 1  # Rock
        case "C":
          return 2  # Paper
        case _:
          return -1
    case "Y":
      match opp_choice:
        case "A":
          return 4
        case "B":
          return 5
        case "C":
          return 6
        case _:
          return -1
    case "Z":
      match opp_choice:
        case "A":
          return 8
        case "B":
          return 9
        case "C":
          return 7
        case _:
          return -1

    case _:
      return -1


with open("data2.txt") as f:
  for line in f:
    final_score += calc_output(line[0], line[2])

print(f"Part 2: {final_score}")
