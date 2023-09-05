# Glorious first attempt that does not work because the names of the dirs repeat (stupid)


def get_sum(key) -> int:
    sum = 0
    sum_kid_dirs = 0

    for value in dir_sizes[key]:
        if value.isdigit():
            sum += int(value)
        else:
            sum += sum_kid_dirs
            sum_kid_dirs = get_sum(value)

    return sum + sum_kid_dirs


current_dir = ["/"]
dir_sizes = dict()
dir_sizes[current_dir[-1]] = []

with open("tdata7.txt") as f:
    next(f, None)
    for line in f:
        if line.find(" ls") == -1 and line.find("dir ") == -1:
            if line.find("cd ..") != -1 and len(current_dir) > 1:
                current_dir.pop()

            elif line.find(" cd ") != -1:
                dir_name = line[5 : line.find("\n")]
                print(dir_name)

                dir_sizes[current_dir[-1]].append(dir_name)
                current_dir.append(dir_name)
                dir_sizes[dir_name] = []

            else:
                dir_sizes[current_dir[-1]].append(line[0 : line.find(" ")])

print(dir_sizes)

dir_sums = dict()
for key in dir_sizes:
    dir_sums[key] = get_sum(key)

final_sum = 0
for key in dir_sums:
    if (dir_sum := dir_sums[key]) <= 100_000:
        final_sum += dir_sum


print(dir_sums)
print(f"Part 1: {final_sum}")
