test_input = """939
7,13,x,x,59,x,31,19"""


def parse_busses(input):
    bus_depart = []
    busses = input[1].strip().split(',')
    start_minute = 0
    for bus in busses:
        if bus.strip() != "x":
            bus_depart.append((int(bus.strip()), start_minute))
        start_minute += 1

    bus_depart.sort()
    highest = bus_depart[-1][1]
    for index in range(0, len(bus_depart)):
        bus_depart[index] = (bus_depart[index][0],
                             bus_depart[index][1]-highest)

    return bus_depart


def determine_time(bus_depart):
    found_time = False
    time_stamp = 0
    counter = 0
    step_size = bus_depart[-1][0]
    print(bus_depart)
    print(f"higest id: {step_size}")
    while not found_time:
        found_time = True
        for bus, start_minute in bus_depart:
            if (time_stamp + start_minute) % bus != 0:
                found_time = False
                break

        if found_time:
            print(f"found: {time_stamp + bus_depart[0][1]}")
            bus_depart.sort(key=lambda x: x[1])
            return time_stamp + bus_depart[0][1]
        time_stamp += step_size
        counter += 1
        if counter % 10000000 == 0:
            print(f"{time_stamp}")


bus_depart = parse_busses(test_input.splitlines())
print(bus_depart)
result = determine_time(bus_depart)
assert result == 1068781

test_input2 = """939,
17,x,13,19"""
bus_depart = parse_busses(test_input2.splitlines())
print(bus_depart)
result = determine_time(bus_depart)
assert result == 3417

test_input3 = """939,
67,7,59,61"""
bus_depart = parse_busses(test_input3.splitlines())
print(bus_depart)
result = determine_time(bus_depart)
assert result == 754018

test_input4 = """939,
67,x,7,59,61"""
bus_depart = parse_busses(test_input4.splitlines())
print(bus_depart)
result = determine_time(bus_depart)
assert result == 779210

test_input5 = """939,
67,7,x,59,61"""
bus_depart = parse_busses(test_input5.splitlines())
print(bus_depart)
result = determine_time(bus_depart)
assert result == 1261476

test_input6 = """939,
1789,37,47,1889"""
bus_depart = parse_busses(test_input6.splitlines())
print(bus_depart)
result = determine_time(bus_depart)
assert result == 1202161486

with open("input.txt", "r") as input_file:
    input = input_file.readlines()

bus_depart = parse_busses(input)
print(bus_depart)
result = determine_time(bus_depart)
print(result)
