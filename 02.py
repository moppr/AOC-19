def intcode_day2(text, noun, verb):
    prog = [int(i) for i in text.split(',')]
    prog[1] = noun
    prog[2] = verb

    i = 0 # instruction pointer
    while True:
        opcode = prog[i]

        if opcode == 1: # SUM
            a,b,c = (prog[i+j] for j in (1,2,3))
            prog[c] = prog[a] + prog[b]
            i += 4
        elif opcode == 2: # PROD
            a,b,c = (prog[i+j] for j in (1,2,3))
            prog[c] = prog[a] * prog[b]
            i += 4

        elif opcode == 99: # HALT
            return prog[0]

        else:
            print(f"Invalid opcode {opcode}")
            return

def find_pair(text):
    for noun in range(100):
        for verb in range(100):
            res = intcode_day2(text, noun, verb)
            if res == 19690720:
                return 100*noun + verb

if __name__ == "__main__":
    with open('02.in') as f:
        text = f.read()
        
        print(intcode_day2(text, 12, 2))
        print(find_pair(text))
