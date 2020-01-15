def find_intersections(text):
    wires=[]
    moveset = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
    for wire in text:
        visited = {}
        x = y = steps = 0
        for move in wire.split(','):
            direction = move[0]
            dist = int(move[1:])
            dx,dy = moveset[direction]
            for i in range(dist):
                x += dx
                y += dy
                steps += 1
                if (x,y) not in visited:
                    visited[(x,y)] = steps
        wires.append(visited)
    intersections = list(set(wires[0].keys()).intersection(wires[1].keys()))
    return min(abs(x)+abs(y) for (x,y) in intersections), min(wires[0][(x,y)]+wires[1][(x,y)] for (x,y) in intersections)

if __name__ == "__main__":
    with open('03.in') as f:
        text = f.readlines()

        print(find_intersections(text))
