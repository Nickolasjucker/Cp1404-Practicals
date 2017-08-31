from random import randrange

MIN = 1
MAX = 45

def method_name():
    count = 0
    number_list = []
    while count != 6:
        generated_num = randrange(MIN, MAX)
        if (generated_num in number_list):
            continue
        number_list.append(generated_num)
        count += 1
    return number_list

def main():
    quickpick_input = int(input("How many quick picks?: "))
    full_list = []
    count = 1
    while count <= quickpick_input:
        full_list.append(method_name())
        count += 1
    for i, num in enumerate(full_list):
        print("{:3} {:3} {:3} {:3} {:3} {:3}".format(num[0], num[1], num[2], num[3], num[4], num[5]))
main()