"""
get name
display menu
get choice
while choice != Q
if choice == H
display "hello" name
else if choice == G
display "goodbye" name
else
display invalid message
display menu
get choice
display finished message
"""
user_name = input("Enter Name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")
menu = input(">>> ")
while menu != "Q":
    if menu == "H":
        print("Hello {}".format(user_name))
    elif menu == "G":
        print("Goodbye {}".format(user_name))
    else:
        print("Invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    menu = input(">>> ")
print("Finished")