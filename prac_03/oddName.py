"""Nickolas Jucker"""
def get_name(name, frequency_input):
    new_name = ""
    correct_input = True
    while correct_input:
        if len(name) > 0:
            remove_space = name.split()
            for i in range(0,len(remove_space), 1):
                new_name = new_name + remove_space[i]
            name_length = len(new_name)
            print(new_name[0:name_length:frequency_input])
            correct_input = False
        else:
            print("Invalid input your name.")
            name = input("What is your name?: ")
def main():
    name = input("What is your name?: ")
    frequency_input = int(input("Enter 1 for every letter
Enter 2 for every second letter
Enter 3 for every third letter
Input: """))
    get_name(name, frequency_input)


main()
