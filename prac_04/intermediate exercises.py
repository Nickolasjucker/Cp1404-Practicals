def main():
    number_list = []
    number_sum = 0
    for i in range(5):
        number_input = int(input("Enter a number: "))
        number_list.append(number_input)
        number_sum += number_list[i]
    number_average = number_sum / 5
    print("The first number is {}".format(number_list[0]))
    print("The last number is {}".format(number_list[4]))
    number_list.sort()
    print("The smallest number is {}".format(number_list[0]))
    print("The largest number is {}".format(number_list[4]))
    print("The average of the numbers is {}".format(number_average))
main()