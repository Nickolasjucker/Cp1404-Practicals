"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
def get_income_per_month(incomes, months):
    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)
    return incomes

def print_income_per_month(incomes, mouth_input):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, mouth_input + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    mouth_input = int(input("How many months? "))

    get_income_per_month(incomes, mouth_input)

    print_income_per_month(incomes, mouth_input)

main()