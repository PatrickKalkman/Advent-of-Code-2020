
passwordFile = open('passwords.txt', 'r')
passwords = passwordFile.readlines()

valid = 0
for policy_line in passwords:
    parts = policy_line.split(" ")
    range = parts[0].split("-")
    check1 = int(range[0]) - 1
    check2 = int(range[1]) - 1
    chr = parts[1].replace(":", "")
    password = parts[2]
    if (password[check1] == chr or password[check2] == chr) and not (password[check1] == chr and password[check2] == chr):
        print(policy_line[:-1] + " = Valid (" +
              password[check1] + "," + password[check2] + ")")
        valid += 1
    else:
        print(policy_line[:-1] + " = Invalid (" +
              password[check1] + "," + password[check2] + ")")

print("Found " + str(valid) + " valid passwords")
