grid = []
visible_trees = 0

with open("data8.txt", "r") as f:
  for line in f:
    grid.append(line.strip())


def check_if_visible(i, j):
  helper_table = [
    [0, i, "vert"],
    [i + 1, len(grid), "vert"],
    [0, j, "horizontal"],
    [j + 1, len(grid[0]), "horizontal"],
  ]

  # if all(grid[k][j] < grid[i][j] for k in range(helper[0], helper[1]))
  for helper in helper_table:
    trees_in_path = []
    for k in range(helper[0], helper[1]):
      if helper[2] == "vert":
        trees_in_path.append(grid[k][j])
      else:
        trees_in_path.append(grid[i][k])

    if max(trees_in_path) < grid[i][j]:
      return 1

  return 0


for i in range(1, len(grid) - 1):
  for j in range(1, len(grid[0]) - 1):
    visible_trees += check_if_visible(i, j)


print(visible_trees)
visible_trees += (len(grid) * 2) + ((len(grid[0]) - 2) * 2)
print(f"Part 1: {visible_trees}")
