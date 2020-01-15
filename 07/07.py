import itertools

def intcode_day7(text, inputs, i=0):
    prog = [int(x) for x in text.split(',')]
    inputs = iter(inputs)
    params = { 1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 99:0 }

    while True:
        raw_opcode = prog[i]
        opcode = raw_opcode % 100
        raw_opcode //= 100
        modes = []
        for _ in range(3): # 3 being max number of parameters
            modes.append(raw_opcode % 10)
            raw_opcode //= 10
        modes = iter(modes)

        indices = [x if next(modes) else prog[x] for x in range(i+1, i+params[opcode]+1)]
                
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
            return prog[a], i
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

        elif opcode == 99: # HALT
            return

        else:
            print(f"Invalid opcode {opcode}")
            return

def single_amplifier(text):
    best = 0
    for phase_set in list(itertools.permutations(list(range(5)))):
        output = 0
        for phase in phase_set:
            curr = intcode_day7(text, [phase, output])
            output = curr[0]            
            best = max(best, output)
    return best

def feedback_loop(text):
    best = 0
    for phase_set in list(itertools.permutations(list(range(5,10)))):
        ips = [0] * 5
        amp = 0
        output = 0
        phase_set = iter(phase_set)
        while True:
            try:
                phase = next(phase_set)
                curr = intcode_day7(text, [phase, output])
            except StopIteration:
                curr = intcode_day7(text, [output], ips[amp])
                
            if curr == None:
                break
            
            output = curr[0]
            ips[amp] = curr[1]
            amp = (amp + 1) % 5
            best = max(best, output)
    return best

if __name__ == "__main__":
    with open('07.in') as f:
        text = f.read()
        print(single_amplifier(text))
        print(feedback_loop(text))
        
