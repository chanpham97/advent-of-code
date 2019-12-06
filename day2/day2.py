def load_mem(file):
    opcodes = open(file)
    mem = opcodes.readline().split(',')
    mem = [int(i) for i in mem] 

    return mem

def process_instruction(mem, ip):
    opcode = mem[ip]
    r1 = mem[ip+1]
    r2 = mem[ip+2]
    d = mem[ip+3]
    val = (mem[r1] + mem[r2]) if (opcode == 1) else (mem[r1] * mem[r2])
    mem[d] = val
    return mem

def process_code(mem):
    ip = 0
    while mem[ip] != 99:
        mem = process_instruction(mem, ip)
        ip = ip + 4
    return mem

    
def main():
    mem = load_mem('day2.txt')
    mem[1] = 12
    mem[2] = 2
    mem = process_code(mem)
    answer1 = mem[0]
    
    for i in range(0, 100):
        for j in range(0, 100):
            mem = load_mem('day2.txt')

            mem[1] = i
            mem[2] = j
            mem = process_code(mem)
            if mem[0] == 19690720:
                answer2 = 100 * i + j
                break
        if mem[0] == 19690720:
            break

    return answer2


print(main())