def find_passwords(text):
    low,high = [int(x) for x in text.split('-')]
    c1 = c2 = 0
    digits = [str(x) for x in range(0, 10)]
    for i in [str(i) for i in range(low, high+1)]:
        if sorted(i) == list(i):
            counts = [i.count(digit) for digit in digits if i.count(digit) >= 2]
            if len(counts) > 0:
                c1 += 1
            if 2 in counts:
                c2 += 1
    return c1, c2

if __name__ == "__main__":
    with open('04.in') as f:
        text = f.read()
        print(find_passwords(text))
