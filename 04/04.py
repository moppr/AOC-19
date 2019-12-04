def find_passwords_part1(text):
    low,high=[int(x) for x in text.split('-')]
    c=0
    for i in [str(i) for i in range(low, high+1)]:
        if sorted(set(i))!=sorted(list(i)) and sorted(list(i)) == list(i):
            c+=1
    return c

def part1_one_liner(text):
    return sum([1 for i in [str(i) for i in range(*[int(x) for x in text.split('-')])] if sorted(set(i))!=sorted(list(i)) and sorted(list(i)) == list(i)])

def find_passwords_part2(text):
    low,high=[int(x) for x in text.split('-')]
    c=0
    r = [x for x in range(0, 10)]
    for i in [str(i) for i in range(low, high+1)]:
        counts = []
        if sorted(list(i)) == list(i):
            for j in r:
                counts.append(i.count(str(j)))
            if 2 in counts:
                c+=1
    return c

if __name__ == "__main__":
    with open('input.txt') as f:
        part = 2

        if part == 1:
            print(find_passwords_part1(f.read()))
            #print(part1_one_liner(f.read()))
        else:
            print(find_passwords_part2(f.read()))
