
def construct_rules(rules_list):
    rules = []
    for rule_line in rules_list:
        parts = rule_line.split("bags contain")
        color_key = parts[0].strip()
        contents = parts[1].split(",")
        internal_colors = []
        for content_part in contents:
            content_part = content_part.strip().replace(
                "bags", "").replace("bag", "").replace(".", "").strip()
            if content_part == "no other":
                color = ""
                amount = 1
            else:
                amount = int(content_part[0:1])
                color = content_part[1:].strip()

            internal_colors.append((color, amount))
        rules.append((color_key, internal_colors))

    return rules


color_counted = []


def construct_rules_tree(rules, sep, start_color):
    number_of_bags = 0
    for top_color, internal_color in rules:
        for color, amount in internal_color:
            if color == start_color:
                if top_color not in color_counted:
                    color_counted.append(top_color)
                    # print(top_color + sep + color)
                    number_of_bags += 1
                    number_of_bags += construct_rules_tree(
                        rules, sep + " -> ", top_color)

    return number_of_bags


color_count = {}


def count_bags_contained(rules, start_color):
    for top_color, internal_color in rules:
        if top_color == start_color:
            if len(internal_color) > 1:
                for color, amount in internal_color:
                    print(f"{top_color}->{amount}*{color}")
                    count_bags_contained(rules, color)


with open('input.txt', 'r') as reader:
    rules = reader.readlines()

rules_parsed = construct_rules(rules)
amount = construct_rules_tree(rules_parsed, " -> ", "shiny gold")
print(amount)

result = count_bags_contained(rules_parsed, "shiny gold")
print(result)
