test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


def find_number(numbers, preamble_size):
    for number_index in range(preamble_size, len(numbers)):
        number = numbers[number_index]

        breaked = False
        start = number_index - preamble_size
        for first_number_index in range(start, start + preamble_size):
            for second_number_index in range(first_number_index + 1, start + preamble_size):
                first = int(numbers[first_number_index])
                second = int(numbers[second_number_index])
                # print(f"{first} + {second} == {number} {first+second}")
                if (first + second == int(number)):
                    breaked = True
                    break
            if breaked:
                break

        if not breaked:
            print(f"Did not find a pattern for {number}")
            return number


def find_number_set(numbers, number_to_find):

    found_first_number_index = 0
    found_second_number_index = 0

    for number_index in range(0, len(numbers)):

        breaked = False
        start = number_index
        for first_number_index in range(start, len(numbers)-1):
            total = int(numbers[first_number_index])
            for second_number_index in range(first_number_index + 1, len(numbers)):
                total += int(numbers[second_number_index])

                if total == int(number_to_find):
                    found_first_number_index = first_number_index
                    found_second_number_index = second_number_index
                    #print(f"{total} == {number_to_find}")
                    breaked = True
                    break
                elif total > int(number_to_find):
                    breaked = False
                    break
            if breaked:
                break

        if breaked:
            # print(
            #    f"{found_first_number_index} {found_second_number_index} {number}")
            return (found_first_number_index, found_second_number_index)

    return (0, 0)


def find_crypt_weakness(input, start_index, end_index):
    numbers = []
    total = 0
    for index in range(start_index, end_index + 1):
        total += int(input[index])
        numbers.append(int(input[index]))

    print(total)
    numbers.sort()
    return int(numbers[0]) + int(numbers[-1])


number = find_number(test_input.splitlines(), 5)
(start_index, end_index) = find_number_set(test_input.splitlines(), number)
weakness = find_crypt_weakness(test_input.splitlines(), start_index, end_index)
print(weakness)

with open("input.txt", "r") as file:
    input = file.readlines()

number = find_number(input, 25)
(start_index, end_index) = find_number_set(input, number)

weakness = find_crypt_weakness(input, start_index, end_index)
print(weakness)
