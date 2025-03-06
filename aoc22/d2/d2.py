# A Rock B Paper C Scissors
# X Rock Y Paper Z Scissors
#    1      2       3
# lost - 0, drew - 3, won- 6

final_score = 0


def evaluate_score(opp_choice: str, choice: str) -> int:
  match choice:
    case "X":
      match opp_choice:
        case "A":
          return 4
        case "B":
          return 1
        case "C":
          return 7
        case _:
          return -1
    case "Y":
      match opp_choice:
        case "A":
          return 8
        case "B":
          return 5
        case "C":
          return 2
        case _:
          return -1
    case "Z":
      match opp_choice:
        case "A":
          return 3
        case "B":
          return 9
        case "C":
          return 6
        case _:
          return -1

    case _:
      return -1


with open("data2.txt") as f:
  for line in f:
    final_score += evaluate_score(line[0], line[2])

print(f"Part 1: {final_score}")
