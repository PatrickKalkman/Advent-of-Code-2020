import copy

test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

test_input_round1_assert = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
"""

test_input_round2_assert = """#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
"""

test_input_round3_assert = """#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
"""


def next_seat(map, row_index, col_index):
    adjacent = 0

    if map[row_index][col_index] == '.':
        return "."

    adjacent += seat_is_taken(map, row_index, col_index, -1, -1)
    adjacent += seat_is_taken(map, row_index, col_index, -1,  0)
    adjacent += seat_is_taken(map, row_index, col_index, -1,  1)

    adjacent += seat_is_taken(map, row_index, col_index,  0, -1)
    adjacent += seat_is_taken(map, row_index, col_index,  0,  1)

    adjacent += seat_is_taken(map, row_index, col_index,  1, -1)
    adjacent += seat_is_taken(map, row_index, col_index,  1,  0)
    adjacent += seat_is_taken(map, row_index, col_index,  1,  1)

    if map[row_index][col_index] == "L" and adjacent == 0:
        return "#"
    elif map[row_index][col_index] == "#" and adjacent > 4:
        return "L"

    return map[row_index][col_index]


def seat_is_taken(map, row_index, col_index, dy, dx):
    iter = 0
    while row_index >= 0 and row_index < len(map) and col_index >= 0 and col_index < len(map[0]):
        iter += 1
        row_index += dy
        col_index += dx
        if row_index < 0 or row_index == len(map):
            return 0

        if col_index < 0 or col_index == len(map[0]):
            return 0

        if map[row_index][col_index] == "#":
            return 1
        elif map[row_index][col_index] == "L":
            return 0

    return 0


def process_seat_round(map):
    processed_map = copy.deepcopy(map)
    for row_index in range(0, len(map)):
        for col_index in range(0, len(map[row_index])):
            content = next_seat(map, row_index, col_index)
            processed_map[row_index][col_index] = content

    return processed_map


def create_map(lines):
    rows = []
    for line in lines:
        cols = []
        for chr in line.strip():
            cols.append(chr)
        rows.append(cols)
    return rows


def count_seats(map):
    seats = 0
    for row in map:
        for col in row:
            if col == "#":
                seats += 1
    return seats


def process_until_stable(original_map):
    previous_map = []
    processed_map = copy.deepcopy(original_map)
    while processed_map != previous_map:
        previous_map = copy.deepcopy(processed_map)
        processed_map = process_seat_round(previous_map)

    return count_seats(processed_map)


map = create_map(test_input.splitlines())
processed_map = process_seat_round(map)
assert_map = create_map(test_input_round1_assert.splitlines())
assert processed_map == assert_map
processed_map = process_seat_round(processed_map)
assert_map = create_map(test_input_round2_assert.splitlines())
assert processed_map == assert_map
processed_map = process_seat_round(processed_map)
assert_map = create_map(test_input_round3_assert.splitlines())
assert processed_map == assert_map

seats = process_until_stable(map)
print(seats)
assert seats == 26

with open("input.txt", "r") as input:
    input_map = input.readlines()

map = create_map(input_map)
seats = process_until_stable(map)
print(seats)
