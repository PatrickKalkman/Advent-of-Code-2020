
expenseFile = open('expenses.txt', 'r')
expenses = expenseFile.readlines()

converted_expenses = [int(expense) for expense in expenses]

for expense1 in converted_expenses:
    for expense2 in converted_expenses:
        for expense3 in converted_expenses:
            if expense1 + expense2 + expense3 == 2020:
                print(str(expense1) + " * " + str(expense2) + " * " +
                      str(expense3) + " = " + str(expense1 * expense2 * expense3))
