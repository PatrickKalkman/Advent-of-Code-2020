map_file = open('map.txt', 'r')
temp_lines = map_file.readlines()
map_lines = [line[:-1] for line in temp_lines]
print("read: " + str(len(map_lines)))

slopes = []
slopes.append((1, 1))
slopes.append((3, 1))
slopes.append((5, 1))
slopes.append((7, 1))
slopes.append((1, 2))

total = []
for slope in slopes:
    col_index = 0
    row_index = 0
    tree_counter = 0
    while row_index < len(map_lines) - 1:
        row_index += slope[1]
        col_index += slope[0]
        string_index = col_index % 31
        if map_lines[row_index][string_index] == "#":
            tree_counter += 1

    print(tree_counter)
    total.append(tree_counter)

print(total[0] * total[1] * total[2] * total[3] * total[4])
