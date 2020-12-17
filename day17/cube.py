import numpy as np

test_input_str = """.#.
..#
###
"""


def build_cube():
    test_input = []
    for line in test_input_str.splitlines():
        test_input_row = []
        for char in line:
            test_input_row.append(char)
        test_input.append(test_input_row)

    cube = np.empty((10, 10, 10), dtype="str")

    for z, set in enumerate(cube):
        for y, col in enumerate(set):
            for x, row in enumerate(set):
                if z == 0 and x < len(test_input[0]) and y < len(test_input):
                    if test_input[y][x] == "#":
                        cube[z, y, x] = test_input[y][x]
    return cube


cube = build_cube()
print(cube[0])
