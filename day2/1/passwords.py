
passwordFile = open('passwords.txt', 'r')
passwords = passwordFile.readlines()

valid = 0
for password in passwords:
    parts = password.split(" ")
    range = parts[0].split("-")
    min = int(range[0])
    max = int(range[1])
    chr = parts[1].replace(":", "")
    passwordPart = parts[2]
    letter_count = 0
    for letter in passwordPart:
        if letter == chr:
            letter_count += 1

    if letter_count >= min and letter_count <= max:
        print(password + " = Valid")
        valid += 1
    else:
        print(password + " = Invalid")


print("Found " + str(valid) + " valid passwords")
