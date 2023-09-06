from functools import reduce

grid = []
max_score = 0

with open("data8.txt") as f:
    for line in f:
        grid.append(line.strip())


def calc_score(i, j):
    helper_table = [
        [0, i, "reverse", "vert"],
        [i + 1, len(grid), "normal", "vert"],
        [0, j, "reverse", "horizontal"],
        [j + 1, len(grid[0]), "normal", "horizontal"],
    ]

    score_table = []

    for helper in helper_table:
        trees_in_path = []
        score = 0
        for k in range(helper[0], helper[1]):
            if helper[3] == "vert":
                trees_in_path.append(grid[k][j])
            else:
                trees_in_path.append(grid[i][k])

        if helper[2] == "reverse":
            trees_in_path.reverse()

        for tree in trees_in_path:
            if tree < grid[i][j]:
                score += 1
            else:
                score += 1
                break
        score_table.append(score)

    # return math.prod(score_table)
    return reduce(lambda x, y: x * y, score_table)


for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if max_score < (score := calc_score(i, j)):
            max_score = score

print(f"Part 2: {max_score}")
