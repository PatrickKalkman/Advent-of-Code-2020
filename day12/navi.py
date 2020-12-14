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

# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship
# is currently facing.


def navigate(instructions):
    face_degrees = 90
    x = 0
    y = 0
    for instr in instructions:
        cleaned_instr = instr.strip()
        dir = cleaned_instr[0]
        value = int(cleaned_instr[1:])

        if dir == "N":
            y += value
        elif dir == "S":
            y -= value
        elif dir == "E":
            x += value
        elif dir == "W":
            x -= value
        elif dir == "L":
            face_degrees -= value
            face_degrees = limit_degrees(face_degrees)
        elif dir == "R":
            face_degrees += value
            face_degrees = limit_degrees(face_degrees)
        elif dir == "F":
            if face_degrees == 0:  # north
                y += value
            elif face_degrees == 90:  # east
                x += value
            elif face_degrees == 180:  # south
                y -= value
            elif face_degrees == 270:  # west
                x -= value

        print(f"{cleaned_instr} {face_degrees}")

    return (x, y)


def limit_degrees(face_degrees):
    if face_degrees >= 360:
        face_degrees -= 360
    if face_degrees < 0:
        face_degrees += 360
    return face_degrees


def calculate_mh(x, y):
    return abs(x) + abs(y)


(x, y) = navigate(test_input.splitlines())
assert x == 17
assert y == -8

mh_distance = calculate_mh(x, y)
assert mh_distance == 25

with open("input.txt", "r") as input_file:
    input = input_file.readlines()

(x, y) = navigate(input)
print(x, y)

mh_distance = calculate_mh(x, y)
print(mh_distance)
