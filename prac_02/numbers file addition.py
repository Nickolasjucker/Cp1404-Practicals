open_file = open("numbers.txt", "r")
number_one = int(open_file.readline())
number_two = int(open_file.readline())
print("The result is {}".format(number_one + number_two))
open_file.close()