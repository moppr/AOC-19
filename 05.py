def intcode_day5(text, inputs):
    prog = [int(i) for i in text.split(',')]
    inputs = iter(inputs)

    i = 0 # instruction pointer
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
            if prog[a]:
                return prog[a]
            i += 2
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
            break

        else:
            print(f"Invalid opcode {opcode}")
            break

if __name__ == "__main__":
    with open('05.in') as f:
        text = f.read()

        print(intcode_day5(text, [1]))
        print(intcode_day5(text, [5]))
