
def decode_boarding_pass(code: str):
    row = decode2('F', code, 0, 0, 127)
    col = decode2('L', code[7:], 0, 0, 7)
    id = row * 8 + col
    return (int(row), int(col), int(id))


def decode(up_char, code, index, start, end, range):

    print(f"{code} {start} {end} {range}")

    if int(range > 1) and code[index] == up_char:
        return decode(up_char, code, index + 1,  start, int(start + range / 2), int(range / 2))
    elif int(range > 1):
        return decode(up_char, code, index + 1, start + int(range / 2), end, int(range / 2))

    if code[index - 1] == up_char:
        return int(start)
    else:
        return int(end)


def decode2(lower_char, code, index, start, end):

    number_of_numbers = int(end - start + 1)
    print(f"{code} {start} {end} {number_of_numbers}")

    if number_of_numbers > 1 and code[index] == lower_char:
        end = int(start + number_of_numbers / 2 - 1)
        index += 1
        return decode2(lower_char, code, index, start, end)
    elif number_of_numbers > 1:
        start = int(start + (number_of_numbers / 2))
        index += 1
        return decode2(lower_char, code, index, start, end)

    return start


col = decode2('L', 'RLR', 0, 0, 7)
assert col == 5
col = decode2('L', 'RRR', 0, 0, 7)
assert col == 7
col = decode2('L', 'RLL', 0, 0, 7)
assert col == 4


row = decode2('F', 'FBFBBFFRLR', 0, 0, 127)
assert row == 44
row = decode2('F', 'BFFFBBFRRR', 0, 0, 127)
assert row == 70
row = decode2('F', 'FFFBBBFRRR', 0, 0, 127)
assert row == 14
row = decode2('F', 'BBFFBBFRLL', 0, 0, 127)
assert row == 102

col = decode2('L', 'RRR', 0, 0, 7)
assert col == 7
col = decode2('L', 'RLL', 0, 0, 7)
assert col == 4

(row, col, id) = decode_boarding_pass('FFFBBBFRRR')
assert row == 14
assert col == 7
assert id == 119

(row, col, id) = decode_boarding_pass('BFFFBBFRRR')
assert row == 70
assert col == 7
assert id == 567

(row, col, id) = decode_boarding_pass('BBFFBBFRLL')
assert row == 102
assert col == 4
assert id == 820

(row, col, id) = decode_boarding_pass('BBFFBBFRLL')
assert row == 102
assert col == 4
assert id == 820

(row, col, id) = decode_boarding_pass('FBFBBFFRLR')
assert row == 44
assert col == 5
assert id == 357

col = decode2('L', 'RLR', 0, 0, 7)
assert col == 5

col = decode2('L', 'RRR', 0, 0, 7)
assert col == 7

with open('input.txt', 'r') as file:
    raw_data = file.readlines()

highest_id = 0
for line in raw_data:
    (row, col, id) = decode_boarding_pass(line.strip())
    if id > highest_id:
        highest_id = id

print(highest_id)

seats = []
for row in range(128):
    cols = []
    for col in range(8):
        cols.append(False)
    seats.append(cols)

for line in raw_data:
    (row, col, id) = decode_boarding_pass(line.strip())
    seats[row][col] = True

for row in range(128):
    for col in range(8):
        if not seats[row][col]:
            print(f"Available {row} {col} {row * 8 + col}")
