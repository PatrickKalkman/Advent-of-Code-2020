test_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""


def execute_program(program):
    memory = {}
    mask = ""
    for instr in program:
        parts = instr.split("=")
        if parts[0].strip() == "mask":
            mask = parts[1].strip()
        else:
            result = ""
            value = int(parts[1].strip())
            address = int(parts[0].replace("mem[", "").replace("]", ""))
            value_binary = f"{value:036b}"
            for index, value_bit in enumerate(value_binary):
                if mask[index] == "X":
                    result += str(value_bit)
                else:
                    result += mask[index]
            memory[address] = int(result, 2)
    return memory


def total_memory_value(memory):
    total = 0
    for key in memory:
        total += memory[key]
    return total


result = execute_program(test_input.splitlines())
total = total_memory_value(result)
assert total == 165
print(total)

with open("input.txt", "r") as file_input:
    input = file_input.readlines()

result = execute_program(input)
total = total_memory_value(result)
print(total)
