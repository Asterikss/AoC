from collections import deque, defaultdict

start = ()
finish = ()
map = defaultdict(lambda: 125)
deq = deque()
visited = set()

with open("data12.txt", "r") as f:
  input = f.readlines()

for i, line in enumerate(input):
  for j, char in enumerate(line.strip()):
    if char == "E":
      map[(i, j)] = ord("z")
      finish = (i, j)
    elif char == "S":
      map[(i, j)] = ord("a")
      deq.append((i, j, 0))
      start = (i, j)
    else:
      if char == "a":
        deq.append((i, j, 0))
      map[(i, j)] = ord(char)

answer = 0

while deq:
  i, j, s = deq.popleft()
  if (i, j) == finish:
    answer = s
    break
  if (i, j) in visited:
    continue
  visited.add((i, j))
  for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    if map[(i + dx, j + dy)] <= map[(i, j)] + 1:
      deq.append((i + dx, j + dy, s + 1))


print(f"Part 2: {answer}")
