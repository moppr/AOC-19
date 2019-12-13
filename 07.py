import itertools

def intcode_day7(text, inputs, i=0):
    prog = [int(i) for i in text.split(',')]
    inputs = iter(inputs)

    while True:
        raw_opcode = prog[i]
        opcode = raw_opcode % 100
        raw_opcode //= 100
        modes = []
        for _ in range(3): # 3 being max number of parameters
            modes.append(raw_opcode % 10)
            raw_opcode //= 10
        modes = iter(modes)

        val = lambda x : i+x if next(modes) == 1 else prog[i+x]

        if opcode == 1: # SUM
            a = val(1)
            b = val(2)
            c = val(3) # should only be mode 0
            prog[c] = prog[a] + prog[b]
            i += 4
        elif opcode == 2: # PROD
            a = val(1)
            b = val(2)
            c = val(3) # should only be mode 0
            prog[c] = prog[a] * prog[b]
            i += 4
        elif opcode == 3: # INPUT
            a = val(1) # should only be mode 0
            prog[a] = next(inputs)
            i += 2
        elif opcode == 4: # OUTPUT
            a = val(1)
            i += 2
            return prog[a], i
        elif opcode == 5: # JMP
            a = val(1)
            b = val(2)
            if prog[a]:
                i = prog[b]
            else:
                i += 3
        elif opcode == 6: # !JMP
            a = val(1)
            b = val(2)
            if not prog[a]:
                i = prog[b]
            else:
                i += 3
        elif opcode == 7: # LT
            a = val(1)
            b = val(2)
            c = val(3) # should only be mode 0
            prog[c] = 1 if prog[a] < prog[b] else 0
            i += 4
        elif opcode == 8: # EQ
            a = val(1)
            b = val(2)
            c = val(3) # should only be mode 0
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
        
