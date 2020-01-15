def intcode_day9(text, inputs=[], i=0):
    prog = [int(x) for x in text.split(',')]
    inputs = iter(inputs)
    base = 0
    params = { 1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 9:1, 99:0 }

    while True:
        raw_opcode = prog[i]
        opcode = raw_opcode % 100
        raw_opcode //= 100
        modes = []
        for _ in range(3): # 3 being max number of parameters
            modes.append(raw_opcode % 10)
            raw_opcode //= 10
        modes = iter(modes)
        
        indices = []
        for x in range(i+1, i+params[opcode]+1): # index of each of the arguments for the current opcode
            m = next(modes)
            if m == 0:
                index = prog[x]
            elif m == 1:
                index = x
            elif m == 2:               
                index = base + prog[x]

            if index < 0:
                raise IndexError(f"Negative index {index} not allowed")
            if index >= len(prog):
                prog += [0] * (index - len(prog) + 1) # these can only really happen if m is 0 or 2
                
            indices.append(index)
                
        a,b,c = indices + [None] * (3 - len(indices)) # safeguard for when indices is less than 3

        if opcode == 1: # SUM
            prog[c] = prog[a] + prog[b]
            i += 4
        elif opcode == 2: # PROD            
            prog[c] = prog[a] * prog[b]
            i += 4
        elif opcode == 3: # INPUT
            prog[a] = next(inputs)
            i += 2
        elif opcode == 4: # OUTPUT
            i += 2
            return prog[a], i # giving back index is vestigial from day 7
        elif opcode == 5: # JMP
            i = prog[b] if prog[a] else i+3
        elif opcode == 6: # !JMP
            i = prog[b] if not prog[a] else i+3
        elif opcode == 7: # LT
            prog[c] = 1 if prog[a] < prog[b] else 0
            i += 4
        elif opcode == 8: # EQ
            prog[c] = 1 if prog[a] == prog[b] else 0
            i += 4
        elif opcode == 9: # BASE
            base += prog[a]
            i += 2
            
        elif opcode == 99: # HALT
            return

        else:
            print(f"Invalid opcode {opcode}")
            return

def boost_program(text):
    return intcode_day9(text, [1])[0], intcode_day9(text, [2])[0]

if __name__ == "__main__":
    with open('09.in') as f:
        text = f.read()
        
        print(boost_program(text))
