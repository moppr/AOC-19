def fun(x, y):
    with open('e.txt') as f:
        arr = f.read().split(',')
        arr = [int(x) for x in arr]
        arr[1] = x
        arr[2] = y
        for i in range(0, len(arr), 4):
            if arr[i] == 99:
                break
            if arr[i] == 1:
                arr[arr[i+3]] = arr[arr[i+2]] + arr[arr[i+1]]
            if arr[i] == 2:
                arr[arr[i+3]] = arr[arr[i+2]] * arr[arr[i+1]]
        #if arr[0] == 19690720:
        #    print("x={} y={} 100*x+y={}".format(x, y, 100*x+y))
        #    return True
        print(arr[0])

def e():        
    for x in range(99):
        for y in range(99):
            if fun(x, y):
                return

#e()
fun(12, 2)
