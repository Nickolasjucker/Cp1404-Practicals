import math
user_input_x = int(input("Enter first number: "))
user_input_y = int(input("Enter second number: "))
print("1. Show even numbers from {} to {}\n2. Show odd numbers from {} to {}\n3. Show the squares from {} to {}\n4. Exit the program".format(user_input_x, user_input_y, user_input_x, user_input_y, user_input_x, user_input_y, ))
menu = input(">>> ")
while menu != "4":
    if menu == "1":
        even = []
        for i in range(user_input_x, user_input_y):
            if i % 2 == 0:
                even.append(i)
        print(even)
    elif menu == "2":
        odd = []
        for i in range(user_input_x, user_input_y):
            if i %2!= 0:
                odd.append(i)
        print(odd)
    elif menu == "3":
        square = list(i**2 for i in range(user_input_x, user_input_y))
        print(square)
    else:
        print("Invalid input")
    print()
    print("1. Show even numbers from {} to {}\n2. Show odd numbers from {} to {}\n3. Show the squares from {} to {}\n4. Exit the program".format(user_input_x, user_input_y, user_input_x, user_input_y, user_input_x, user_input_y, ))
    menu = input(">>> ")