test_input1 = """16
10
15
5
1
11
7
19
6
12
4
"""


test_input2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


def find_best_next_adapter(initial_jolt, adapters):
    smallest_adapter = 32000
    smallest_dif = 32000

    if len(adapters) == 1:
        return adapters[0]

    for adapter in adapters:
        diff = int(adapter) - initial_jolt
        if (diff < smallest_dif):
            smallest_dif = diff
            smallest_adapter = adapter

    return smallest_adapter


def construct_adapter_chain(adapters):
    len_adapters = len(adapters)
    adapter_chain = []
    initial_adapter = 0
    while len(adapter_chain) != len_adapters:
        print(f"{len(adapter_chain)} - {len_adapters}")
        adapter = find_best_next_adapter(
            initial_adapter, adapters)
        if adapter == 32000:
            print("Breaking")
            break
        print(adapter)
        adapter_chain.append(adapter)
        adapters.remove(adapter)
    return adapter_chain


def count_differences(chain):
    diff_count = {}
    for index in range(len(chain) - 1):
        diff = int(chain[index + 1]) - int(chain[index])
        if diff in diff_count:
            diff_count[diff] += 1
        else:
            diff_count[diff] = 1
    return diff_count


def add_start_and_device_adapter(chain):
    top = chain[-1]
    chain.insert(0, "0")
    chain.append(str(int(top) + 3))
    return chain


def count_paths(adapters):

    adapters.append(0)
    adapters.append(max(adapters) + 3)

    output = adapters[-1]

    num_ways = [0] * (output + 1)

    num_ways[0] = 1

    if 1 in adapters:
        num_ways[1] = 1

    if 2 in adapters and 1 in adapters:
        num_ways[2] = 2
    elif 2 in adapters:
        num_ways[2] = 1

    for n in range(3, output+1):
        if n not in adapters:
            continue

        num_ways[n] = num_ways[n-3] + num_ways[n-2] + num_ways[n-1]

    return num_ways[output]


chain = construct_adapter_chain(test_input1.splitlines())
chain = add_start_and_device_adapter(chain)
print(chain)
diff_count = count_differences(chain)
print(diff_count)

chain = construct_adapter_chain(test_input2.splitlines())
chain = add_start_and_device_adapter(chain)
print(chain)
diff_count = count_differences(chain)
print(diff_count)

with open("input.txt", "r") as file:
    input = file.readlines()

print(f"input = {len(input)}")
stripped_input = []
for line in input:
    stripped_input.append(line.strip())

chain = construct_adapter_chain(stripped_input)
print(f"len = {len(chain)}")
chain = add_start_and_device_adapter(chain)
print(chain)
diff_count = count_differences(chain)
print(diff_count)

test_list = [int(i) for i in test_input1.splitlines()]
result = count_paths(test_list)
print(result)


test_list2 = [int(i) for i in test_input2.splitlines()]
result = count_paths(test_list2)
print(result)


test_list3 = [int(i) for i in input]
result = count_paths(test_list3)
print(result)
