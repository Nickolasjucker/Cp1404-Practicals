"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
def main():
    sales = float(input("Enter sales: $ "))
    under_sales = 0.1
    over_sales = 0.15
    while sales >= 0:
        if sales >= 1000:
            print("You earned $", sales, "with a bonus of", sales * over_sales)
            sales = float(input("Enter sales: $ "))
        else:
            print("You earned $", sales, "with a bonus of", sales * under_sales)
            sales = float(input("Enter sales: $ "))
    print("You lost $", sales, "and no bonus received")
main()