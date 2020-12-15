import time

with open('input.txt', 'r') as reader:
    original_code = reader.readlines()

test_code = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def run_until_second_time(code):
    keep_running = True
    code_visited = []

    code_index = 0
    acc = 0
    while keep_running:
        instruction = code[code_index].strip()
        if code_index in code_visited:
            print(f"stop! acc={acc}")
            return False
        code_visited.append(code_index)
        # print(f"exec: {instruction} acc = {acc}")
        parts = instruction.split(" ")
        if parts[0] == "acc":
            acc += int(parts[1])
            code_index += 1
        elif parts[0] == "nop":
            code_index += 1
        elif parts[0] == "jmp":
            code_index += int(parts[1])

        if code_index == len(code):
            print(f"exec correctly: acc = {acc}")
            return True


def mutate_code(code, start_index):
    changed_code = []
    changed = False
    changed_index = 0

    if start_index >= len(code) - 1:
        print("end")
        return ([], 0)

    if start_index > 0:
        for code_index in range(0, start_index):
            instruction = code[code_index].strip()
            changed_code.append(instruction)

    for code_index in range(start_index, len(code)):
        instruction = code[code_index].strip()
        if instruction.split(" ")[0] == "nop" and not changed:
            changed_code.append(instruction.replace("nop", "jmp"))
            changed = True
            changed_index = code_index
            # print(f"changed {instruction} {changed_index}")
        elif instruction.split(" ")[0] == "jmp" and not changed:
            changed_code.append(instruction.replace("jmp", "nop"))
            changed = True
            changed_index = code_index
            # print(f"changed {instruction} {changed_index}")
        else:
            changed_code.append(instruction)

    return (changed_code, changed_index + 1)


run_until_second_time(test_code.splitlines())

search_index = 0
start_index = 0
valid = False
while not valid:
    code, start_index = mutate_code(original_code, start_index)

    # print(f"{len(code)} {len(original_code)}")
    # print(f"{start_index}")
    # print(f"{code[start_index-1]} {original_code[start_index-1]}")

    #code, start_index = mutate_code(original_code, start_index)

    # print(f"{len(code)} {len(original_code)}")
    # print(f"{start_index}")
    # print(f"{code[start_index-5].split()} {original_code[start_index-5].split()}")
    # print(f"{code[start_index-4].split()} {original_code[start_index-4].split()}")
    # print(f"{code[start_index-3].split()} {original_code[start_index-3].split()}")
    # print(f"{code[start_index-2].split()} {original_code[start_index-2].split()}")
    # print(f"{code[start_index-1].split()} {original_code[start_index-1].split()}")

    # exit()
    # for index in range(0, len(original_code) - 1):
    #     if original_code[index].strip() == code[index].strip():
    #         print(
    #             f"{index} {original_code[index].strip()} = {code[index].strip()}")
    #     else:
    #         print(
    #             f"--> {index} {original_code[index].strip()} = {code[index].strip()}")

    if len(code) > 0:
        valid = run_until_second_time(code)
    else:
        valid = True
