def find_cross_part1(text):
    wires=[]
    moveset = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
    for wire in text:
        seen = []
        x = y = 0
        moves = [i for i in wire.split(',')]
        for move in moves:
            direction = move[0]
            dist = int(move[1:])
            dx,dy = moveset[direction]
            for i in range(dist):
                x += dx
                y += dy
                seen.append((x,y))
        wires.append(seen)
    intersections = list(set(wires[0]).intersection(wires[1]))
    return min([abs(x)+abs(y) for (x,y) in intersections])

def find_cross_part2(text):
    wires=[]
    moveset = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
    for wire in text:
        seen = {}
        x = y = steps = 0
        moves = [i for i in wire.split(',')]
        for move in moves:
            direction = move[0]
            dist = int(move[1:])
            dx,dy = moveset[direction]
            for i in range(dist):
                x += dx
                y += dy
                steps += 1
                seen[(x,y)] = steps
        wires.append(seen)
    intersections = list(set(wires[0].keys()).intersection(wires[1].keys()))
    return min([wires[0][(x,y)]+wires[1][(x,y)] for (x,y) in intersections])

if __name__ == "__main__":
    with open('input.txt') as f:
        part = 2

        if part == 1:
            print(find_cross_part1(f.readlines()))
        else:
            print(find_cross_part2(f.readlines()))
