def find_passwords_part1(text):
    low,high=[int(x) for x in text.split('-')]
    c=0
    # assumes that the password is automatically 6 digits since the start and end
    # ranges seem to always be 6 digits too
    for i in [str(i) for i in range(low, high+1)]:
        # first condition ensures there is at least one double
        # second condition ensures the password is in order
        if sorted(set(i))!=sorted(list(i)) and sorted(list(i)) == list(i):
            c+=1
    return c

def part1_one_liner(text):
    # condensed version of above, except generates list of 1s and sums it
    # instead of using a counter (much less memory efficient but more fun)
    return sum([1 for i in [str(i) for i in range(*[int(x) for x in text.split('-')])] if sorted(set(i))!=sorted(list(i)) and sorted(list(i)) == list(i)])

def find_passwords_part2(text):
    low,high=[int(x) for x in text.split('-')]
    c=0
    r = [x for x in range(0, 10)]
    for i in [str(i) for i in range(low, high+1)]:
        # keep track of occurrences of each digit
        # groups of 3 or more are invalid
        # but as long as there's a group of 2 it's ok, even if there's a 3+ group
        # this could have been used for part 1 as well
        # by checking 2-6 instead of just 2
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
