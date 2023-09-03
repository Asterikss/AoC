
with open("data6.txt") as f:
    input = f.read()

    for i in range(len(input) - 14):
        if len(set(input[i:i+14])) == len(input[i:i+14]):
            print(input[i:i+14])
            print(f"Part 2: {i + 14}")
            break
