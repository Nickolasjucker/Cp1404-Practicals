def main():
    name = input("What is your name?: ")
    get_name(name)

def get_name(name):
    correct_input = True
    while correct_input:
        if len(name) > 0:
            remove_space = name.strip()
            name_length = len(remove_space)
            print_name(name_length, remove_space)
            correct_input = False
        else:
            print("Invalid input your name.")
            name = input("What is your name?: ")

def print_name(name_length, remove_space):
    print(remove_space[1:name_length:2])

main()
