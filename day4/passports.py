with open('passports.txt', 'r') as file:
    raw_data = file.readlines()

passports = []
passport = {}

for line in raw_data:
    if line == '\n':
        passports.append(passport)
        passport = {}
    else:
        fields = line.split(' ')
        for field in fields:
            keyvalue = field.split(':')
            passport[keyvalue[0]] = keyvalue[1].strip()

passports.append(passport)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.


def is_valid_byr(value):
    if value.isnumeric():
        year = int(value)
        return year >= 1920 and year <= 2020
    return False

# iyr (Issue Year) - four digits; at least 2010 and at most 2020.


def is_valid_iyr(value):
    if value.isnumeric():
        year = int(value)
        return year >= 2010 and year <= 2020
    return False

# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.


def is_valid_eyr(value):
    if value.isnumeric():
        year = int(value)
        return year >= 2020 and year <= 2030
    return False

# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.


def is_valid_hgt(height):
    if 'cm' in height:
        value = height.replace('cm', '')
        if value.isnumeric():
            height = int(value)
            return height >= 150 and height <= 193
    elif 'in' in height:
        value = height.replace('in', '')
        if value.isnumeric():
            height = int(value)
            return height >= 59 and height <= 76

    return False

# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.


def is_valid_hcl(value):
    allowed_chars = '0123456789abcdef'
    if value[0] == '#' and len(value) == 7:
        chars = value[1:]
        for char in chars:
            if char not in allowed_chars:
                return False
        return True
    return False

# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.


def is_valid_ecl(value):
    allowed_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return value in allowed_colors

# pid (Passport ID) - a nine-digit number, including leading zeroes.


def is_valid_pid(value):
    return len(value) == 9 and value.isnumeric()


required_fields = [
    ('byr', is_valid_byr),
    ('iyr', is_valid_iyr),
    ('eyr', is_valid_eyr),
    ('hgt', is_valid_hgt),
    ('hcl', is_valid_hcl),
    ('ecl', is_valid_ecl),
    ('pid', is_valid_pid)
]


invalid_passports = 0
for passport in passports:
    for required_field, is_valid in required_fields:
        if required_field not in passport:
            print(f"{passport} is not valid, missing {required_field}")
            invalid_passports += 1
            break
        else:
            if not is_valid(passport[required_field]):
                print(
                    f"{passport} is not valid, field {required_field}:{passport[required_field]} is not valid")
                invalid_passports += 1
                break

print(f"Passports: {len(passports)}")
print(f"Invalid: {invalid_passports}")
print(f"Valid: {len(passports) - invalid_passports}")
