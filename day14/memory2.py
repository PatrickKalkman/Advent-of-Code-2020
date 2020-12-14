test_input = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
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
            address = int(parts[0].replace("mem[", "").replace("]", ""))
            address_binary = f"{address:036b}"
            for index, address_bit in enumerate(address_binary):
                if mask[index] == "X":
                    result += "X"
                elif mask[index] == "0":
                    result += address_bit
                else:
                    result += "1"

            x_count = result.count("X")

            value = int(parts[1].strip())
            bin_size = pow(2, x_count)
            for bin_count in range(bin_size):
                binary = f"{bin_count:0{x_count}b}"
                new_address = result
                for bit in binary:
                    new_address = new_address.replace("X", bit, 1)

                address = int(new_address, 2)
                memory[address] = value

    return memory


def total_memory_value(memory):
    total = 0
    for key in memory:
        total += memory[key]
    return total


result = execute_program(test_input.splitlines())
total = total_memory_value(result)
assert total == 208
print(total)

with open("input.txt", "r") as file_input:
    input = file_input.readlines()

result = execute_program(input)
total = total_memory_value(result)
print(total)


# 000000000000000000000000000000X1101X
