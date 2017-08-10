def main():
    item_price_list = []
    item_quantity = int(input("Number of items: "))
    i = 0
    while item_quantity <= 0:
        print("Invalid Input")
        item_quantity = int(input("Number of items: "))
    else:
        while i < item_quantity:
            i = i + 1
            item_price = float(input("Price of item: $"))
            item_price_list.append(item_price)
        total_price = sum(item_price_list)
        if total_price > 100:
            discount_price = total_price * 0.1
            print("Total price for", item_quantity, "items is", total_price - discount_price)
        else:
            print("Total price for", item_quantity, "items is", total_price)
main()