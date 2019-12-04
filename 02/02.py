def intcode_part1(text):
    # turn full intcode input into array
    arr = [int(i) for i in text.split(',')]
    # program inputs
    arr[1] = 12
    arr[2] = 2
    #i represents each instruction pointer, perform operation based on it
    for i in range(0, len(arr), 4):
        if arr[i] == 99:
            break
        if arr[i] == 1:
            arr[arr[i+3]] = arr[arr[i+2]] + arr[arr[i+1]]
        if arr[i] == 2:
            arr[arr[i+3]] = arr[arr[i+2]] * arr[arr[i+1]]
    print(arr[0])

def intcode_part2(x, y, text):
    arr = [int(i) for i in text.split(',')]
    arr[1] = x
    arr[2] = y
    for i in range(0, len(arr), 4):
        if arr[i] == 99:
            break
        if arr[i] == 1:
            arr[arr[i+3]] = arr[arr[i+2]] + arr[arr[i+1]]
        if arr[i] == 2:
            arr[arr[i+3]] = arr[arr[i+2]] * arr[arr[i+1]]
    if arr[0] == 19690720:
        print("x={} y={} 100*x+y={}".format(x, y, 100*x+y))
        return True
        
def find_pair(text):
    # brute force which pair of inputs gets 19690720
    for x in range(99):
        for y in range(99):
            if intcode_part2(x, y, text):
                return

if __name__ == "__main__":
    with open('input.txt') as f:
        part=2

        if part==1:
            intcode_part1(f.read())
        else:
            find_pair(f.read())
