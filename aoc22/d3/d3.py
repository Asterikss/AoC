
final_score = 0

with open("data3.txt") as f:
    for line in f:
        stripped_line = line.strip()

        first_half = line[0:int(len(line)/2)]
        second_half = line[int(len(line)/2):-1]

        char_found = ""
        for char in first_half:
            if char in second_half:
                char_found = char

        print(char_found)
    
        # if char_found.islower():
        if char_found == char_found.lower():
            print(ord(char_found) - 96)
            final_score += ord(char_found) - 96
        else:
            print(ord(char_found) - 64 + 26)
            final_score += ord(char_found) - 64 + 26


print(f"Part 1: {final_score}")






