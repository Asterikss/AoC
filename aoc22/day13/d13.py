with open("data13.txt") as f:
    input = f.readlines()

indexs = []


# -1 - left smaller; 0 - the same; 1 - right smaller
def compare_list(left, right) -> int:
    result = 0
    for l, r in zip(left, right):
        if type(l) == int and type(r) == int:
            result = compare_element(l, r)
        elif type(l) == list and type(r) == list:
            result = compare_list(l, r)
        elif type(l_list := l) != type(r_list := r):
            if type(l) == int:
                l_list = [l]
            else:
                r_list = [r]
            result = compare_list(l_list, r_list)

        if result != 0:
            return result

    if len(right) < len(left):
        return 1
    return -1


def compare_element(left, right) -> int:
    if left < right:
        return -1
    if left == right:
        return 0
    return 1


for i in range(0, len(input), 3):
    result = compare_list(eval(input[i]), eval(input[i + 1]))
    if not result == 1:
        indexs.append((i / 3) + 1)

print(f"Part 1: {int(sum(indexs))}")
