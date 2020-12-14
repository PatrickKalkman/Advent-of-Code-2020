test_input = """939
7,13,x,x,59,x,31,19"""


def get_depart_time(input):
    earliest = int(input[0].strip())
    busses = input[1].strip().replace("x,", "").split(',')

    best_bus = 0
    time_diff = 6000

    for bus in busses:
        bus_div = int(earliest / int(bus))
        bus_mod = earliest % int(bus)

        if bus_mod != 0:
            depart = (bus_div + 1) * int(bus)
        else:
            depart = bus_div * int(bus)

        bus_diff = depart - earliest
        if bus_diff < time_diff:
            time_diff = bus_diff
            best_bus = bus

    print(best_bus)
    print(time_diff)
    return int(best_bus) * time_diff


result = get_depart_time(test_input.splitlines())
print(result)

with open("input.txt", "r") as input_file:
    input = input_file.readlines()

result = get_depart_time(input)
print(result)
