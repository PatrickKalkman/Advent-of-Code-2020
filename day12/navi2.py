import math

test_input = """F10
N3
F7
R90
F11
"""
#
#     N
# W       E
#     S
#
# start face east

# Action N means to move the waypoint north by the given value.
# Action S means to move the waypoint south by the given value.
# Action E means to move the waypoint east by the given value.
# Action W means to move the waypoint west by the given value.
# Action L means to rotate the waypoint around the ship left
# (counter-clockwise)the given number of degrees.
# Action R means to rotate the waypoint around the ship right (clockwise)
# the given number of degrees.
# Action F means to move forward to the waypoint a number of times equal
#  to the given value.


def navigate(instructions):
    waypoint_x = 10
    waypoint_y = 1

    ship_x = 0
    ship_y = 0
    for instr in instructions:
        cleaned_instr = instr.strip()
        dir = cleaned_instr[0]
        value = int(cleaned_instr[1:])

        if dir == "N":
            waypoint_y += value
        elif dir == "S":
            waypoint_y -= value
        elif dir == "E":
            waypoint_x += value
        elif dir == "W":
            waypoint_x -= value
        elif dir == "L":
            waypoint_x, waypoint_y = calculate_new_pos(
                waypoint_x, waypoint_y, value)
        elif dir == "R":
            waypoint_x, waypoint_y = calculate_new_pos(
                waypoint_x, waypoint_y, -value)
        elif dir == "F":
            ship_x += value * waypoint_x
            ship_y += value * waypoint_y

        # print(
        #   f"{instr} => waypoint ({waypoint_x},{waypoint_y}) ship ({ship_x},{ship_y})")

    return (ship_x, ship_y)


def calculate_mh(x, y):
    return abs(x) + abs(y)


def calculate_new_pos(x, y, degrees):
    rad = math.radians(degrees)
    new_x = int(round(x * math.cos(rad) - y * math.sin(rad)))
    new_y = int(round(x * math.sin(rad) + y * math.cos(rad)))
    return (new_x, new_y)


(x, y) = navigate(test_input.splitlines())
print(x, y)
assert x == 214
assert y == -72

mh_distance = calculate_mh(x, y)
assert mh_distance == 286

with open("input.txt", "r") as input_file:
    input = input_file.readlines()

(x, y) = navigate(input)
print(x, y)

mh_distance = calculate_mh(x, y)
print(mh_distance)
