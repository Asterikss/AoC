from functools import cmp_to_key

with open("data13.txt") as f:
    input = f.readlines()

indexs = []
fixed_input = []


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


def sort_fixed_input():
    for i in range(len(fixed_input) - 1, 0, -1):
        result = compare_list(fixed_input[i], fixed_input[i - 1])
        if result == -1:
            tmp = fixed_input[i]
            fixed_input[i] = fixed_input[i - 1]
            fixed_input[i - 1] = tmp
        else:
            return i
    return -1


fixed_input.append(eval(input[0]))
for i in range(1, len(input)):
    if len(input[i]) != 1:
        fixed_input.append(eval(input[i]))
        sort_fixed_input()

fixed_input.append([[2]])
first_idx = sort_fixed_input() + 1
fixed_input.append([[6]])
second_idx = sort_fixed_input() + 1

for fx in fixed_input:
    print(fx)

fixed_input2 = [eval(line.strip()) for line in input if line.strip()]
fixed_input2.extend([[[2]], [[6]]])
fixed_input2 = sorted(fixed_input2, key=cmp_to_key(compare_list))
res = 1
for i, line in enumerate(fixed_input2):
    if line in [[[2]], [[6]]]:
        res *= i + 1

print(f"Part 2: {first_idx * second_idx}")
print(f"Second method Part 2: {res}")
