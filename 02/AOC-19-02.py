def intcode(x, y):
    with open('input.txt') as f:
        arr = [int(i) for i in f.read().split(',')]
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
        
def find_pair():        
    for x in range(99):
        for y in range(99):
            if intcode(x, y):
                return

if __name__ == "__main__":
    find_pair()
