import re
from functools import cache


class Valve:
    def __init__(self, name, flow_rate, neighbours) -> None:
        self.name = name
        self.flow_rate = flow_rate
        self.neighbours = neighbours
        self.opened = False


@cache
def walk(current: Valve, time: int) -> int:
    if time == 0:
        return 0

    score = max(walk(v, time - 1) for v in current.neighbours)

    if current.flow_rate > 0 and not current.opened:
        current.opened = True
        score = max(score, (time - 1) * current.flow_rate + walk(current, time - 1))

    return score


valve_vec = []

with open("tdata16.txt") as f:
    for line in f:
        neighbours = []
        words = re.split(r", | ", line.strip())
        current = words[1]
        flow_rate = int(words[4][words[4].find("=") + 1 : -1])
        counter = -1

        while words[counter] not in ["valves", "valve"]:
            neighbours.append(words[counter])
            counter -= 1

        valve_vec.append(Valve(current, flow_rate, neighbours))

for v in valve_vec:
    new_neighbours = []
    for n in v.neighbours:
        new_neighbours.append([v for v in valve_vec if v.name == n][0])
    v.neighbours = new_neighbours


print(f"Part 1: {walk(valve_vec[0], 30)}")
