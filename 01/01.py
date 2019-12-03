def fuel(mass):
    return mass//3-2

def sum_part1(text):
    return sum([fuel(int(line)) for line in text])

def sum_part2(text):
    total = 0
    for line in text:
        curr = int(line)
        while curr > 0:
            curr = fuel(curr)
            total += max(0, curr)
    return total

if __name__ == "__main__":
    with open('input.txt') as f:
        part = 1

        if part == 1:
            print(sum_part1(f.readlines()))
        else:
            print(sum_part2(f.readlines()))
