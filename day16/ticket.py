test_input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

rules = {}
ticket = []
nearby = []


def parse_input(input):

    RULES = 1
    TICKET = 2
    OTHER = 3

    state = RULES

    for line in input:

        if line.strip() == "":
            continue
        if line.strip() == "your ticket:":
            state = TICKET
            continue
        elif line.strip() == "nearby tickets:":
            state = OTHER
            continue
        if state == RULES:
            rule = line.split(":")
            rule_key = rule[0].strip()
            ranges = rule[1].split("or")
            numbers1 = ranges[0].split("-")
            numbers2 = ranges[1].split("-")
            range1 = (int(numbers1[0]), int(numbers1[1]))
            range2 = (int(numbers2[0]), int(numbers2[1]))
            rules[rule_key] = (range1, range2)
        elif state == TICKET:
            ticket_numbers = line.strip().split(",")
            for ticket_number in ticket_numbers:
                ticket.append(int(ticket_number))
        elif state == OTHER:
            other_tickets = []
            ticket_numbers = line.strip().split(",")
            for ticket_number in ticket_numbers:
                other_tickets.append(int(ticket_number))
            nearby.append(other_tickets)


def find_invalid_ticket_numbers():
    error_rate = 0
    for ticket in nearby:
        for number in ticket:
            number_valid = False
            for rule in rules:
                (lower1, higher1), (lower2, higher2) = rules[rule]
                if number >= lower1 and number <= higher1 or number >= lower2 and number <= higher2:
                    number_valid = True
            if not number_valid:
                error_rate += number
    return error_rate


def remove_invalid_tickets():
    tickets_to_remove = []
    for ticket in nearby:
        for number in ticket:
            number_valid = False
            for rule in rules:
                (lower1, higher1), (lower2, higher2) = rules[rule]
                if number >= lower1 and number <= higher1 or number >= lower2 and number <= higher2:
                    number_valid = True
            if not number_valid:
                tickets_to_remove.append(ticket)

    for invalid_ticket in tickets_to_remove:
        nearby.remove(invalid_ticket)


rules_order = []


def identify_fields():
    for number_index in range(20):
        selected_key = ""
        for key in rules:
            print(f"validating {key}")
            (lower1, higher1), (lower2, higher2) = rules[key]
            valid = True
            for ticket in nearby:
                number = ticket[number_index]
                if (number >= lower1 and number <= higher1) or (number >= lower2 and number <= higher2):
                    valid = True
                else:
                    print(ticket)
                    print(number)
                    valid = False
                    break
            if valid:
                selected_key = key
                break
        if selected_key != "":
            print(f"{selected_key} {number_index}")
            rules_order.append(selected_key)
            del rules[selected_key]


# Test
parse_input(test_input.splitlines())
result = find_invalid_ticket_numbers()
assert result == 71

# 1
rules = {}
ticket = []
nearby = []

with open("input.txt", "r") as input_file:
    input = input_file.readlines()

parse_input(input)
result = find_invalid_ticket_numbers()
print(result)

# 2
rules = {}
ticket = []
nearby = []

with open("input.txt", "r") as input_file:
    input = input_file.readlines()

parse_input(input)
remove_invalid_tickets()
identify_fields()

for index, rule in enumerate(rules_order):
    if "departure" in rule:
        print(ticket[index])
