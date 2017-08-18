"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
UNDER_SALES = 0.1
OVER_SALES = 0.15
def main():
    sales = float(input("Enter sales: $ "))
    while sales >= 0:
        if sales >= 1000:
            print("You earned ${:.2f} with a bonus of ${:.2f}".format(sales, sales * OVER_SALES))
        else:
            print("You earned ${:.2f}  with a bonus of ${:.2f}".format(sales, sales * UNDER_SALES))
        sales = float(input("Enter sales: $ "))
main()