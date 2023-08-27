
with open("data1.txt") as f:
    input = f.read()

counter: int = 0
number_str: str = ""
sum_number_int: int = 0
maks: list[int] = [0, 0, 0]

def check_sum(number: int):
    maks.sort(reverse=True)
    if maks[-1] < number:
        maks[-1] = number


for char in input:
    if char == "\n":
        counter+=1

        if counter == 2:
            check_sum(sum_number_int)
            sum_number_int = 0
            counter = 0

        else:
            sum_number_int += int(number_str)
            number_str = ""

    else:
        number_str += char
        counter = 0

print(f"Part 1: {max(maks)}")
print(f"Part 2: {sum(maks)}")
