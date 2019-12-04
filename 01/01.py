def fuel(mass):
    return mass//3-2

def sum_part1(text):
    # perform fuel formula on each module and sum all results
    return sum([fuel(int(line)) for line in text])

def sum_part2(text):
    total = 0
    # need to calculate fuel total per module first before summing
    for line in text:
        curr = int(line)
        # recalculate fuel based on what was just added
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
